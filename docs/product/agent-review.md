---
title: Agent review
description: Why every connected-agent change waits for a person in Deckastra.
---

# Agents prepare. People decide.

Every change from a connected agent waits for human approval. An MCP client can read within its grant, create structured proposals, preview work, and withdraw its own pending proposal. It cannot approve a proposal or mint sharing authority.

## What Review shows

- The request and attributable source.
- Changed slides and before/after results.
- The unchanged authoritative deck beside the proposal.
- **Play motion** for proposed animation.
- Explicit **Approve** and **Reject** decisions.

![Assistant drawer with a pending proposal](/screenshots/09-ai-proposal.png)

![Side-by-side proposal review](/screenshots/10-proposal-review.png)

## Stale work is refused

Each proposal carries the revision it was authored against. If the deck has changed in a way that makes the proposal unsafe to apply, the user is asked to reject it and request fresh work. Draft Board uses the equally direct warning **Deck changed too**.

## Reversible and attributable

Approved operations enter the same transaction and version systems as direct edits. History records what changed and which surface authored it; undo, inverse operations, and restore preserve a route back.

::: warning Release verification gate
The public submission asserts that every connected-agent change waits for approval. The submitted application build must be verified against that behavior before publication.
:::
