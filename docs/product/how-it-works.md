---
title: How it works
---

# How Deckastra works

<div class="journey"><div><strong>Express intent</strong><span>Author directly, choose a template, ask the assistant, or connect an agent.</span></div><div><strong>Build a proposal</strong><span>Intent becomes structured operations against a known deck revision.</span></div><div><strong>Validate and review</strong><span>The schema, media rules, and current revision are checked before a person decides.</span></div><div><strong>Compose and deliver</strong><span>Deterministic engines produce the scene used for editing, presenting, and export.</span></div></div>

## One canonical model

`.mydeck` is the source of truth. React components, DOM nodes, timelines, PowerPoint shapes, and preview images are temporary representations derived from it.

<ArchitecturePanel image="/diagrams/03-generation-rendering.svg" title="Generation and deterministic rendering" caption="Models and agents stay at the intent boundary; code owns geometry and rendering." />

## Review before authority changes

Connected-agent work is presented as a proposal. Review shows the unchanged deck and the proposed result, can play pending motion, and refuses a stale proposal instead of forcing it onto a newer revision.

<ArchitecturePanel image="/diagrams/04-change-proposal-lifecycle.svg" title="Change proposal lifecycle" caption="A person remains the approval authority between an external agent and the saved deck." />

## Preserve the story of the work

Accepted transactions produce versioned, attributable history and inverse operations. Recovery journals, backups, and export job records add further recovery boundaries.
