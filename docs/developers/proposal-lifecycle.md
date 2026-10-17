---
title: Proposal lifecycle
---

# Proposal lifecycle

<ArchitecturePanel image="/diagrams/04-change-proposal-lifecycle.svg" title="Human and agent change lifecycle" caption="Connected agents prepare structured operations; the application validates and a person decides." />

1. The client reads the deck and current revision.
2. It prepares bounded, id-addressed operations.
3. Deckastra validates schema, semantics, media integrity, scope, and expected revision.
4. The proposal remains pending while Review renders before and after.
5. A person approves or rejects it; motion can be previewed before the decision.
6. Approval applies one attributable transaction and creates history with an inverse.
7. A stale proposal is refused and must be re-authored against the new revision.

An MCP client can withdraw its own pending work. It cannot approve work, decide another author’s proposal, or create public sharing authority.
