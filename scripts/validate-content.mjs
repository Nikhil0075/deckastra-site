import { createHash } from 'node:crypto'
import { readdir, readFile } from 'node:fs/promises'
import { extname, join, relative } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = fileURLToPath(new URL('../', import.meta.url))
const docsRoot = fileURLToPath(new URL('../docs/', import.meta.url))
const publicRoot = fileURLToPath(new URL('../docs/public/', import.meta.url))
const errors = []

async function walk(directory) {
  const entries = await readdir(directory, { withFileTypes: true })
  const files = []
  for (const entry of entries) {
    const path = join(directory, entry.name)
    if (entry.isDirectory() && !['.vitepress', 'node_modules'].includes(entry.name)) files.push(...await walk(path))
    else if (entry.isFile()) files.push(path)
  }
  return files
}

const publicDocs = (await walk(docsRoot)).filter(file => ['.md', '.ts', '.vue'].includes(extname(file)))
const forbidden = [
  { pattern: /C:\\Users\\ROG/gi, label: 'personal local path' },
  { pattern: /D:\\Presentation_app/gi, label: 'private repository path' },
  { pattern: /nikhilranjanmurmu75@gmail\.com/gi, label: 'personal email' },
  { pattern: /A low-risk change applies immediately/gi, label: 'stale approval claim' },
  { pattern: /gha-creds-[\w.-]+\.json/gi, label: 'temporary credential filename' },
  { pattern: /-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----/g, label: 'private key' }
]

for (const file of publicDocs) {
  const text = await readFile(file, 'utf8')
  for (const rule of forbidden) {
    if (rule.pattern.test(text)) errors.push(`${relative(root, file)} contains ${rule.label}`)
    rule.pattern.lastIndex = 0
  }
  if (extname(file) !== '.md') continue
  for (const match of text.matchAll(/!\[([^\]]*)\]\(([^)]+)\)/g)) {
    if (!match[1].trim()) errors.push(`${relative(root, file)} has an image without alt text: ${match[2]}`)
  }
  for (const match of text.matchAll(/\[[^\]]+\]\((\/[^)#?]+)(?:[)#?][^)]*)?\)/g)) {
    const link = match[1]
    if (link.startsWith('/screenshots/') || link.startsWith('/diagrams/') || link.startsWith('/brand/')) continue
    const route = link.replace(/^\//, '').replace(/\/$/, '')
    const candidates = [join(docsRoot, `${route}.md`), join(docsRoot, route, 'index.md')]
    let found = false
    for (const candidate of candidates) {
      try { await readFile(candidate); found = true; break } catch {}
    }
    if (!found) errors.push(`${relative(root, file)} links to missing route ${link}`)
  }
}

const manifest = JSON.parse(await readFile(new URL('./public-assets.json', import.meta.url), 'utf8'))
for (const [name, expected] of Object.entries(manifest)) {
  const bytes = await readFile(join(publicRoot, name))
  const actual = createHash('sha256').update(bytes).digest('hex')
  if (bytes.byteLength !== expected.bytes || actual !== expected.sha256) errors.push(`Public asset changed without manifest refresh: ${name}`)
}

const actualScreenshots = (await readdir(join(publicRoot, 'screenshots'))).filter(name => /\.(png|jpg)$/i.test(name))
const actualDiagrams = (await readdir(join(publicRoot, 'diagrams'))).filter(name => name.endsWith('.svg'))
if (actualScreenshots.length !== 34) errors.push(`Expected 34 screenshots, found ${actualScreenshots.length}`)
if (actualDiagrams.length !== 8) errors.push(`Expected 8 SVG diagrams, found ${actualDiagrams.length}`)

const toolsPage = await readFile(new URL('../docs/developers/mcp-tools.md', import.meta.url), 'utf8')
const toolNames = [...toolsPage.matchAll(/\| `([a-z_]+)` \|/g)].map(match => match[1])
if (new Set(toolNames).size !== 50) errors.push(`Expected 50 unique MCP tools, found ${new Set(toolNames).size}`)

if (errors.length) {
  console.error(errors.map(error => `- ${error}`).join('\n'))
  process.exit(1)
}

console.log(`Validated ${publicDocs.length} public source files, ${actualScreenshots.length} screenshots, ${actualDiagrams.length} diagrams, and ${toolNames.length} MCP tools.`)
