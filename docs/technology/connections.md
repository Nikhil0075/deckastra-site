---
title: Data and connections
---

# Important connections

- **Web → API → Cloud SQL:** authenticated cloud presentation and account workflows.
- **Desktop → local sidecar:** local workspace authority, files, history, and recovery.
- **MCP server → desktop authority:** scoped reads and pending proposals while Deckastra is running.
- **API → providers:** server-held credentials for translation, voice, speech, and governed media.
- **Worker → jobs → object storage:** isolated rendering and export delivery.
- **Presenter → audience window:** current frame, reveal state, black screen, and ink.

<ArchitecturePanel image="/diagrams/07-auth-storage-export-connections.svg" title="Authentication, storage, and export" caption="Credentials, data, jobs, and downloadable artifacts cross named boundaries." />

Desktop local decks remain distinct from cloud/web decks. Account deletion cannot remove files or exported copies that exist only on a user’s computer.
