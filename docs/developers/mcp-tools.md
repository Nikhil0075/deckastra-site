---
title: MCP tool reference
description: The 50 MCP tools exposed by Deckastra, grouped by workflow.
---

# MCP tool reference

Deckastra exposes **50 tools**. This public reference is grouped by task rather than internal source order. Every tool that changes a deck prepares work for human review; no tool can approve its own result.

## Workspace and document reading

| Tool | Purpose |
|---|---|
| `workspace_list` | List visible workspaces, projects, decks, and the currently open deck. |
| `document_read` | Read a compact deck outline and element identities. |
| `document_read_slide` | Read one slide’s exact structured values. |
| `slide_preview` | Render the current or proposed result for one slide. |
| `document_versions` | Read recent version history and authorship. |
| `design_check` | Run deterministic layout, contrast, order, and editability checks. |

## Deck creation and composition

| Tool | Purpose |
|---|---|
| `document_create` | Create an empty deck. |
| `preset_list` | List reviewed deck templates and named slots. |
| `deck_from_template` | Build a schema-valid deck from a reviewed template. |
| `deck_compose` | Compose a deck from structured story intent. |
| `slide_insert_pattern` | Insert a reviewed slide pattern. |
| `style_suggest` | Prepare two to four reviewed visual directions. |
| `theme_propose` | Propose accessible deck colors and typography. |
| `design_language_get` | Read one design language’s grammar and limits. |

## Draft Board

| Tool | Purpose |
|---|---|
| `draft_create` | Create a geometry-free planning board. |
| `draft_list` | List boards in a project. |
| `draft_read` | Read the latest board revision and cards. |
| `draft_update` | Revise cards with optimistic concurrency. |

## Proposals and requests

| Tool | Purpose |
|---|---|
| `document_propose` | Submit id-addressed patch operations as a pending proposal. |
| `proposal_list` | List changes waiting for a person’s decision. |
| `proposal_withdraw` | Withdraw the calling client’s own pending proposal. |
| `request_list` | List persisted questions attached to a deck or draft. |
| `request_answer` | Attach findings or proposal alternatives to a request. |

## Media

| Tool | Purpose |
|---|---|
| `asset_list` | List workspace media. |
| `asset_view` | Inspect one media asset. |
| `asset_update` | Update safe metadata such as alt text. |
| `asset_duplicates` | Find duplicate media identities. |
| `media_quote` | Quote governed picture or video generation. |
| `media_generate` | Request governed media generation. |
| `image_quote` | Quote an image-specific generation request. |
| `image_generate` | Generate an image after quotation. |
| `image_import_prepare` | Prepare a controlled image import. |
| `image_import_propose` | Propose an imported image for the workspace. |
| `media_place` | Propose placing an approved asset on a slide. |

## Motion

| Tool | Purpose |
|---|---|
| `motion_capabilities` | Read supported presets, pacing, roles, and budgets. |
| `motion_propose` | Propose a semantic entrance sequence. |
| `object_motion_propose` | Propose entrance, emphasis, loop, or exit motion. |
| `ambient_motion_propose` | Add restrained background motion to selected slides. |
| `transition_propose` | Propose a slide transition or reviewed morph pairing. |
| `motion_style_apply` | Apply a reviewed motion vocabulary across a deck. |
| `motion_preview` | Render time-labelled frames from a current or pending timeline. |

## Languages and narration

| Tool | Purpose |
|---|---|
| `locale_list` | Read languages and missing or outdated text slots. |
| `locale_add` | Add an empty language overlay. |
| `locale_propose` | Propose translations for named text slots. |
| `narration_propose` | Add or rewrite narration aligned to click steps. |
| `voice_quote` | Quote synthesis for existing narration lines. |
| `voice_lines` | Synthesize quoted lines and word timing. |

## Export

| Tool | Purpose |
|---|---|
| `document_export` | Start a PDF or PowerPoint export job. |
| `export_status` | Read progress and the final degradation ledger. |
| `export_cancel` | Cancel an export that has not completed. |

The exact schema and behavior remain authoritative in the main repository’s MCP server implementation. Clients should discover tool schemas from the running server rather than hand-authoring undocumented request fields.
