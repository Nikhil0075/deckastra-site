---
title: Architecture
---

# Technical architecture

> Agents propose structured intent, deterministic engines compose, and humans approve reviewable changes.

Deckastra is a monorepo of reusable document, transaction, layout, rendering, animation, export, application, and agent components. The canonical `.mydeck` model connects them without making any one UI the source of truth.

<ArchitecturePanel image="/diagrams/01-system-context.svg" title="System context" caption="People and agents meet at a structured, human-controlled presentation authority." />

<ArchitecturePanel image="/diagrams/02-monorepo-components.svg" title="Monorepo components" caption="Shared packages drive desktop, web, API, worker, and MCP surfaces." />

<ArchitecturePanel image="/diagrams/03-generation-rendering.svg" title="Generation and rendering" caption="Intent is composed, validated, resolved to a scene, and rendered consistently." />

<ArchitecturePanel image="/diagrams/04-change-proposal-lifecycle.svg" title="Proposal lifecycle" caption="Versioned proposals preserve review, stale-write protection, and human authority." />
