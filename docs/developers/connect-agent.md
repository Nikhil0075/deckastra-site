---
title: Connect an agent
---

# Connect an agent

## Before you start

Deckastra must be open. Go to **Settings → Agents**, choose the client, copy the configuration generated for the installed location, and select **Allow agent access**. Permission lasts up to twelve hours and starts off after a fresh install or upgrade.

When a client attaches, Deckastra shows **Agent connected**. Stopping access removes the attachment and revokes issued grants.

## Claude Code

Copy Deckastra’s generated `.mcp.json` block into the project root:

```json
{
  "mcpServers": {
    "deckastra": {
      "command": "C:/Users/<you>/AppData/Local/Programs/Deckastra/Deckastra.exe",
      "args": ["C:/Users/<you>/AppData/Local/Programs/Deckastra/resources/mcp/cli.mjs"],
      "env": {
        "ELECTRON_RUN_AS_NODE": "1",
        "DECKASTRA_MCP_CLIENT": "claude-code"
      }
    }
  }
}
```

Restart or reload MCP connections, then ask the client to list Deckastra workspaces. Keep absolute paths.

## Codex

Copy Deckastra’s generated block into `~/.codex/config.toml`:

```toml
[mcp_servers.deckastra]
command = "C:/Users/<you>/AppData/Local/Programs/Deckastra/Deckastra.exe"
args = ["C:/Users/<you>/AppData/Local/Programs/Deckastra/resources/mcp/cli.mjs"]
env = { ELECTRON_RUN_AS_NODE = "1", DECKASTRA_MCP_CLIENT = "codex" }
```

Restart the MCP connection and ask Codex to list the open workspace or deck.

## Authority model

The grant permits scoped reads, write proposals, and export work. It does not permit approval, sharing, or bypassing workspace authority. Every agent-origin change waits for human approval. A proposal against an older revision receives a stale conflict instead of overwriting the deck.

`DECKASTRA_MCP_CLIENT` is an audit label, not a credential. The protected attachment credential expires with the application session.

## Troubleshooting

- Start Deckastra, enable access, then restart the MCP server if it is unreachable.
- Reconnect with the newly generated configuration after an upgrade.
- Read the current deck and propose again after a stale conflict.
- Verify `ELECTRON_RUN_AS_NODE=1`, absolute paths, and client logs if the connection chip does not appear.
