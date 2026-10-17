import { createHash } from 'node:crypto'
import { readdir, readFile, writeFile } from 'node:fs/promises'
import { join, relative } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = fileURLToPath(new URL('../docs/public/', import.meta.url))

async function walk(directory) {
  const entries = await readdir(directory, { withFileTypes: true })
  const files = []
  for (const entry of entries) {
    const path = join(directory, entry.name)
    if (entry.isDirectory()) files.push(...await walk(path))
    else files.push(path)
  }
  return files
}

const files = (await walk(root)).sort()
const manifest = {}
for (const file of files) {
  const bytes = await readFile(file)
  manifest[relative(root, file).replaceAll('\\', '/')] = {
    bytes: bytes.byteLength,
    sha256: createHash('sha256').update(bytes).digest('hex')
  }
}

await writeFile(new URL('./public-assets.json', import.meta.url), `${JSON.stringify(manifest, null, 2)}\n`)
console.log(`Recorded ${files.length} public assets.`)
