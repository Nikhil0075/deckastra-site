---
title: Troubleshooting
---

# Troubleshooting

## “This cloud feature is switched off”

Provider-backed AI, translation, or speech may be disabled by configuration or the AI-only budget stop. Local editing can remain healthy. Retry later or ask the operator to verify provider status.

## Sign-in or credits are required

Open the account menu and sign in. Confirm the app shows the plan and remaining credits. Capture the stable error code, reason, hint, and request ID if a cloud action still fails.

## “Built from different migrations”

The shell, local service, and database do not describe the same release. Close Deckastra and install a matching complete release. Do not replace only the sidecar or copy database files between versions.

## Unsaved work after the workspace service stops

Keep the editor open, use **Retry** after the service returns, and download the emergency copy first if offered. Confirm **Saved** and inspect version history afterward.

## “Proposal is out of date” or “Deck changed too”

Reject or discard stale work and ask the agent to create a new proposal against the latest revision. Do not force the old patch onto the new deck.

![The stale-edit guard offering Merge, Discard mine, and Keep editing](/screenshots/37-stale-edit-guard.png)

## SmartScreen or Gatekeeper blocks the installer

The beta is unsigned. Verify the official filename and SHA-256 before using the platform’s manual approval flow. Stop if the checksum differs.

## Agent cannot connect

Deckastra must be running. Open **Settings → Agents**, select the client, copy the current configuration, and choose **Allow agent access**. Access expires, is revoked when stopped, and defaults off after upgrades.
