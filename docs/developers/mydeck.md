---
title: .mydeck format
---

# `.mydeck` format overview

`.mydeck` is Deckastra’s canonical packaged presentation format. Structured JSON is validated by shared schemas; media and fonts have explicit identities rather than being flattened into slide screenshots.

## Core concepts

- Document metadata, viewport, theme, and language overlays.
- Ordered slides with stable IDs.
- Typed elements with geometry, semantic roles, style, and content.
- Charts, tables, diagrams, equations, code, and media references.
- Animation tracks, triggers, transitions, narration cues, and timing.
- Provenance, accessibility data, and export semantics.
- Patch operations, revisions, validation, and inverse transactions.

Clients operate against an expected revision. Stale mutations are refused.

::: warning Contract boundary
This overview is not a standalone serialization specification. The schema, presentation core, transactions, workspace contracts, and package tests in the main repository remain authoritative. Consumers should use those packages rather than inventing fields.
:::
