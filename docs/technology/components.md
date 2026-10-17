---
title: Application components
---

# Application components

| Component | Responsibility |
|---|---|
| `.mydeck` schema | Canonical typed presentation model and validation authority. |
| Presentation core | Pure document operations that emit patches. |
| Transactions | Patch apply, inverses, undo/redo, and lifecycle. |
| Editor | Selection, hit testing, transforms, snapping, clipboard, and rich-text editing. |
| Layout engine | Text measurement, constraints, and deterministic container layout. |
| Renderer | Document → IntermediateScene → DOM/SVG and render digests. |
| Animation engine | Presets, timeline compilation, sampling, and playback adapters. |
| Export adapters | Shared capability contract plus PDF and PowerPoint output. |
| API | Composition, persistence, versions, proposals, jobs, identity, and provider gateways. |
| Desktop shell | Electron application and local workspace authority. |
| Web app | Browser editor and cloud-backed workflows. |
| Worker | Headless rendering and export jobs. |
| MCP server | Scoped tools through which compatible agents read and propose. |

The `.mydeck` document remains the authority. Selection, hover, camera position, DOM nodes, and rendered previews do not become saved presentation state.
