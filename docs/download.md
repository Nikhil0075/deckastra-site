---
title: Download Deckastra
description: Download the unsigned Deckastra 0.9.0 beta for macOS or check Windows and web availability.
---

# Download Deckastra

Deckastra `0.9.0-beta.1` is beta software. Open the hosted web application or download the macOS beta. Desktop builds are unsigned, so verify the exact filename and SHA-256 before opening them.

<DownloadCards />

## macOS installation

The available build targets Apple-silicon Macs. After downloading the DMG, verify its checksum, move Deckastra to Applications, and try to open it. If Gatekeeper blocks the unsigned beta, go to **System Settings → Privacy & Security**, verify the app name and source, and use the offered approval action.

Verify from Terminal:

```bash
shasum -a 256 Deckastra-0.9.0-beta.1-mac-arm64.dmg
```

Expected result:

```text
9312FE790F38A405862FDFC2059D0AC3389B05FE10341E462146190B473A800E
```

## Windows status

The x64 installer exists and has been hashed, but its public release URL is not yet available. The download remains disabled until the published artifact returns successfully and matches the recorded SHA-256.

## Requirements and boundaries

- Internet is required for sign-in and cloud-backed generation, translation, voices, or speech.
- Core local editing does not require those providers.
- A second display is optional for the presenter console.
- A final Windows/macOS version, CPU, RAM, and disk support matrix has not been accepted; this page does not invent one.
