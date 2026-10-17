---
title: Technical stack
---

# Technical stack

| Layer | Technology |
|---|---|
| Desktop | Electron 44, React, TypeScript |
| Web | Next.js 16, React 19 |
| API | FastAPI, SQLAlchemy |
| Database | PostgreSQL 16 / Cloud SQL |
| Infrastructure | Terraform, Google Cloud |
| Rendering | React/SVG and deterministic scene model |
| Exports | PDF and OOXML/PowerPoint |
| Agent integration | Model Context Protocol |
| Tests | Vitest, Pytest, browser and acceptance harnesses |

## Contract strategy

Zod schemas are the normative document definitions. Generated JSON Schema feeds Python validation, MCP schemas, and external tooling. CI fails when the committed schema artifact or fixtures drift from the source.

## Determinism strategy

Fixed-iteration layout, explicit number formatting, recorded font fallback, inlined icons, and a shared IntermediateScene reduce differences between the editor, browser renderer, PDF, and PowerPoint paths.
