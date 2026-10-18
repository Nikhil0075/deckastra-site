import { defineConfig } from 'vitepress'

const repository = 'https://github.com/Nikhil0075/deckastra'

export default defineConfig({
  title: 'Deckastra',
  description: 'Presentations with agent speed and human control.',
  lang: 'en-US',
  base: '/deckastra-site/',
  cleanUrls: true,
  appearance: false,
  lastUpdated: true,
  sitemap: { hostname: 'https://nikhil0075.github.io/deckastra-site/' },
  head: [
    ['link', { rel: 'icon', href: '/deckastra-site/favicon.ico' }],
    ['meta', { name: 'theme-color', content: '#ffffff' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'Deckastra — agent speed, human control' }],
    ['meta', { property: 'og:description', content: 'Structured, editable presentations with reviewable agent proposals.' }],
    ['meta', { property: 'og:image', content: 'https://nikhil0075.github.io/deckastra-site/brand/og-card.png' }],
    ['meta', { property: 'og:image:width', content: '1200' }],
    ['meta', { property: 'og:image:height', content: '630' }],
    ['meta', { property: 'og:image:alt', content: 'Deckastra: presentations with agent speed and human control' }],
    ['meta', { name: 'twitter:image', content: 'https://nikhil0075.github.io/deckastra-site/brand/og-card.png' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }]
  ],
  themeConfig: {
    logo: '/brand/deckastra-mark.png',
    siteTitle: 'Deckastra',
    search: { provider: 'local' },
    nav: [
      {
        text: 'Product',
        items: [
          { text: 'Overview', link: '/product/' },
          { text: 'The problem', link: '/product/problem' },
          { text: 'Features', link: '/product/features' },
          { text: 'How it works', link: '/product/how-it-works' },
          { text: 'Agent review', link: '/product/agent-review' },
          { text: 'Motion & presenting', link: '/product/motion-presenting' },
          { text: 'Languages & narration', link: '/product/languages-narration' },
          { text: 'Export & recovery', link: '/product/export-recovery' }
        ]
      },
      {
        text: 'Technology',
        items: [
          { text: 'Architecture', link: '/technology/' },
          { text: 'Components', link: '/technology/components' },
          { text: 'Cloud', link: '/technology/cloud' },
          { text: 'Connections', link: '/technology/connections' },
          { text: 'Scalability', link: '/technology/scalability' },
          { text: 'Security & trust', link: '/technology/security-trust' },
          { text: 'Technical stack', link: '/technology/stack' }
        ]
      },
      { text: 'Guides', link: '/guide/' },
      {
        text: 'Developers',
        items: [
          { text: 'Overview', link: '/developers/' },
          { text: 'Connect an agent', link: '/developers/connect-agent' },
          { text: 'MCP tools', link: '/developers/mcp-tools' },
          { text: '.mydeck format', link: '/developers/mydeck' },
          { text: 'Proposal lifecycle', link: '/developers/proposal-lifecycle' },
          { text: 'Example prompts', link: '/developers/prompts' }
        ]
      },
      { text: 'Hackathon', link: '/hackathon/' },
      { text: 'Open Web App', link: 'https://deckastra-web-fwqqltaqta-el.a.run.app/' },
      { text: 'Download', link: '/download' },
      { text: 'GitHub', link: repository }
    ],
    sidebar: {
      '/product/': [{
        text: 'Product',
        items: [
          { text: 'Overview', link: '/product/' },
          { text: 'The problem', link: '/product/problem' },
          { text: 'Features', link: '/product/features' },
          { text: 'How it works', link: '/product/how-it-works' },
          { text: 'Agent review', link: '/product/agent-review' },
          { text: 'Motion & presenting', link: '/product/motion-presenting' },
          { text: 'Languages & narration', link: '/product/languages-narration' },
          { text: 'Export & recovery', link: '/product/export-recovery' }
        ]
      }],
      '/technology/': [{
        text: 'Technology',
        items: [
          { text: 'Architecture', link: '/technology/' },
          { text: 'Application components', link: '/technology/components' },
          { text: 'Cloud architecture', link: '/technology/cloud' },
          { text: 'Data & connections', link: '/technology/connections' },
          { text: 'Scalability', link: '/technology/scalability' },
          { text: 'Security & trust', link: '/technology/security-trust' },
          { text: 'Technical stack', link: '/technology/stack' }
        ]
      }],
      '/guide/': [
        {
          text: 'Getting started',
          items: [
            { text: 'Guide home', link: '/guide/' },
            { text: 'Installation', link: '/guide/install' },
            { text: 'First deck', link: '/guide/first-deck' },
            { text: 'Interface tour', link: '/guide/interface' }
          ]
        },
        {
          text: 'Common tasks',
          items: [
            { text: 'Rename a deck', link: '/guide/tasks/rename' },
            { text: 'Work with templates', link: '/guide/tasks/templates' },
            { text: 'Add media', link: '/guide/tasks/media' },
            { text: 'Review agent changes', link: '/guide/tasks/review' },
            { text: 'Add motion', link: '/guide/tasks/motion' },
            { text: 'Translate a deck', link: '/guide/tasks/translation' },
            { text: 'Add narration', link: '/guide/tasks/narration' },
            { text: 'Present with ink', link: '/guide/tasks/presenting' },
            { text: 'Export a deck', link: '/guide/tasks/export' },
            { text: 'Recover work', link: '/guide/tasks/recovery' }
          ]
        },
        {
          text: 'Reference',
          items: [
            { text: 'Keyboard shortcuts', link: '/guide/shortcuts' },
            { text: 'Troubleshooting', link: '/guide/troubleshooting' },
            { text: 'Glossary', link: '/guide/glossary' },
            { text: 'Credits & privacy', link: '/guide/credits-privacy' }
          ]
        }
      ],
      '/developers/': [{
        text: 'Developers',
        items: [
          { text: 'Overview', link: '/developers/' },
          { text: 'Connect an agent', link: '/developers/connect-agent' },
          { text: 'MCP tool reference', link: '/developers/mcp-tools' },
          { text: '.mydeck format', link: '/developers/mydeck' },
          { text: 'Proposal lifecycle', link: '/developers/proposal-lifecycle' },
          { text: 'Example prompts', link: '/developers/prompts' }
        ]
      }],
      '/hackathon/': [{
        text: 'Hackathon',
        items: [
          { text: 'Submission overview', link: '/hackathon/' },
          { text: 'Demo walkthrough', link: '/hackathon/demo' },
          { text: 'Technical achievements', link: '/hackathon/achievements' },
          { text: 'Evidence gallery', link: '/hackathon/evidence' },
          { text: 'Current limitations', link: '/hackathon/limitations' },
          { text: 'Roadmap', link: '/hackathon/roadmap' }
        ]
      }]
    },
    socialLinks: [{ icon: 'github', link: repository }],
    editLink: { pattern: 'https://github.com/Nikhil0075/deckastra-site/edit/main/docs/:path', text: 'Edit this page on GitHub' },
    footer: {
      message: 'Deckastra 0.9.0-beta.1 · Unsigned beta software',
      copyright: 'Built in public with human approval at the boundary.'
    },
    outline: { level: [2, 3], label: 'On this page' },
    lastUpdated: { text: 'Updated' },
    docFooter: { prev: 'Previous', next: 'Next' }
  }
})
