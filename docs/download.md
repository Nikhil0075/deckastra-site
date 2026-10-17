---
title: Download Deckastra
description: Download the unsigned Deckastra 0.9.0 beta for Windows or macOS, or open the web application.
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

## Windows installation

The x64 installer is published through Deckastra's public installer storage. It is unsigned, so Windows SmartScreen may show **Windows protected your PC**. Compare the downloaded file's SHA-256 with the value on the card. If it matches, choose **More info** and then **Run anyway**.

## Requirements and boundaries

- Internet is required for sign-in and cloud-backed generation, translation, voices, or speech.
- Core local editing does not require those providers.
- A second display is optional for the presenter console.
- A final Windows/macOS version, CPU, RAM, and disk support matrix has not been accepted; this page does not invent one.
