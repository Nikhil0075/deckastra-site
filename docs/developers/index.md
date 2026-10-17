---
title: Developer overview
---

# Developer overview

Deckastra exposes structured presentation workflows to compatible agents through a bundled Model Context Protocol server. Agents can inspect workspaces and decks, create or compose decks, work with draft boards, submit proposals, manage approved media, propose motion and language overlays, and start exports.

## Start here

1. [Connect Claude Code or Codex](/developers/connect-agent).
2. Read the [50-tool MCP reference](/developers/mcp-tools).
3. Understand the canonical [`.mydeck` format](/developers/mydeck).
4. Follow the [proposal lifecycle](/developers/proposal-lifecycle).
5. Adapt the [example prompts](/developers/prompts).

## Authority boundary

Agent access is local, explicit, scoped, time-bounded, and revocable. A connected agent may prepare work, but every agent-origin edit stays pending until a person approves it in Deckastra. The MCP surface contains no approval or share-link authority.

<ArchitecturePanel image="/diagrams/05-desktop-local-runtime.svg" title="Desktop local runtime" caption="The bundled MCP server attaches to the running desktop authority rather than editing files behind its back." />
