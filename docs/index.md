---
layout: page
title: Deckastra
description: Structured, editable presentations with agent speed and human control.
sidebar: false
aside: false
editLink: false
lastUpdated: false
---

<script setup>
import { withBase } from 'vitepress'
const pillars = [
  { icon: '◇', title: 'Structured, not flattened', text: 'Text, charts, diagrams, code, motion, narration, and media remain addressable objects in the canonical .mydeck document.', link: './product/features' },
  { icon: '⌁', title: 'Deterministic composition', text: 'Agents propose intent. Deckastra’s layout, renderer, animation, and export engines turn it into reproducible output.', link: './technology/' },
  { icon: '✓', title: 'Approval is the boundary', text: 'Agent work stays pending until you compare the result and decide. Stale work cannot silently overwrite a newer deck.', link: './product/agent-review' }
]
const features = [
  { icon: '✦', title: 'Direct authoring', text: 'Build and refine real slide objects with a visual canvas, structured inspection, and deterministic Design Check.', link: './product/features' },
  { icon: '◫', title: 'Templates & languages', text: 'Start from reviewed templates and distinct design languages, then keep full editing control.', link: './guide/tasks/templates' },
  { icon: '↔', title: 'Agent proposals', text: 'Connect Claude Code, Codex, or another MCP client without handing it approval authority.', link: './developers/connect-agent' },
  { icon: '▶', title: 'Motion & presenting', text: 'Author reveals, transitions, and object motion; present with notes, timing, ink, and a second screen.', link: './product/motion-presenting' },
  { icon: '文', title: 'Languages & narration', text: 'Maintain language overlays, live voice choices, pronunciation hints, and click-aligned narration.', link: './product/languages-narration' },
  { icon: '⇩', title: 'Export with context', text: 'Export PDF or editable PowerPoint and read what the target format flattened or changed.', link: './product/export-recovery' }
]
const metrics = [
  { value: '50', label: 'MCP tools' },
  { value: '34', label: 'current product captures' },
  { value: '8', label: 'architecture diagrams' },
  { value: '48', label: 'keyboard shortcuts' }
]
</script>

<HeroPanel />

<section class="home-section">
  <p class="section-kicker">The product thesis</p>
  <h2>Agents propose. Deterministic engines compose. Humans approve.</h2>
  <p class="section-intro">Presentation creation should not force a choice between manual control and automation. Deckastra keeps the document structured, the output reproducible, and the final authority with the person making the deck.</p>
  <FeatureGrid :items="pillars" />
</section>

<section class="home-section">
  <p class="section-kicker">One studio, complete workflow</p>
  <h2>From first idea to the room where you present it.</h2>
  <FeatureGrid :items="features" />
</section>

<section class="trust-band">
  <p class="section-kicker">Human approval, by design</p>
  <h2>An agent can prepare the change. It cannot make the decision.</h2>
  <p>Every connected-agent edit appears as a reviewable proposal. Compare before and after, play proposed motion, approve or reject, and refuse stale work when the deck has moved.</p>
  <a class="button secondary" href="./product/agent-review">Explore the review boundary</a>
</section>

<section class="home-section">
  <p class="section-kicker">How it works</p>
  <h2>A short path from intent to a deck you can trust.</h2>
  <div class="journey"><div><strong>Express intent</strong><span>Start directly, from a reviewed template, with the assistant, or through an agent.</span></div><div><strong>Compose structure</strong><span>Typed intent becomes a validated .mydeck document and deterministic scene.</span></div><div><strong>Review change</strong><span>Compare proposed work against the current revision before it changes the deck.</span></div><div><strong>Present or export</strong><span>Use the same scene across the editor, presenter, PDF, and PowerPoint adapters.</span></div></div>
  <ArchitecturePanel image="/diagrams/01-system-context.svg" title="System context" caption="One structured document connects people, agents, deterministic engines, presentation, and export." />
</section>

<section class="home-section">
  <p class="section-kicker">Evidence, not mockups</p>
  <h2>Current product surfaces, captured from the running application.</h2>
  <p class="section-intro">Filter the gallery to inspect authoring, agent review, motion, presentation, language, recovery, export, and settings states.</p>
  <ProofMetrics :items="metrics" />
  <EvidenceGallery />
</section>

<section class="home-section split-section">
  <div>
    <p class="section-kicker">Hackathon submission</p>
    <h2>Media, Content & Digital Experiences.</h2>
    <p class="section-intro">Deckastra is a submission to <a href="https://aibuildercup.com/">AI Builder Cup</a>. It brings together desktop and web surfaces, 50 agent tools, reviewable proposals, deterministic rendering, live language and voice workflows, and PDF/PowerPoint export.</p>
    <div class="hero-actions"><a class="button primary" href="./hackathon/">Follow the judge journey</a><a class="button secondary" href="./download">Get the beta</a><a class="text-link" href="https://aibuildercup.com/">AI Builder Cup →</a></div>
  </div>
  <img class="split-art" :src="withBase('/illustrations/agent-approval.jpg')" alt="An AI agent proposes a change to a stack of slides while a person approves it" width="1200" height="896" loading="lazy">
</section>
