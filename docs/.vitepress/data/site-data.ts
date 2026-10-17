export interface SiteLinks {
  github: string
  issues: string
  releases: string
  webApp?: string
}

export interface DownloadArtifact {
  platform: 'Windows' | 'macOS' | 'Web'
  architecture: string
  filename?: string
  version: string
  status: 'available' | 'pending'
  signature: 'unsigned beta' | 'not applicable'
  url?: string
  byteSize?: number
  sha256?: string
  releaseDate?: string
  warning: string
}

export interface EvidenceItem {
  id: string
  category: 'Authoring' | 'Agents' | 'Motion' | 'Presentation' | 'Languages' | 'Recovery' | 'Export' | 'Settings'
  image: string
  title: string
  caption: string
  alt: string
  surface: 'desktop'
  verified: string
}

export const siteLinks: SiteLinks = {
  github: 'https://github.com/Nikhil0075/deckastra',
  issues: 'https://github.com/Nikhil0075/deckastra/issues',
  releases: 'https://github.com/Nikhil0075/deckastra/releases',
  webApp: 'https://deckastra-web-794139896808.asia-south1.run.app/'
}

export const downloads: DownloadArtifact[] = [
  {
    platform: 'Web', architecture: 'Browser', version: 'Release 8', status: 'available', signature: 'not applicable',
    url: 'https://deckastra-web-794139896808.asia-south1.run.app/',
    warning: 'Hosted directly on Google Cloud Run for the hackathon. This link opens the application UI, not the API service.'
  },
  {
    platform: 'Windows', architecture: 'x64', filename: 'Deckastra-0.9.0-beta.1-win-x64.exe', version: '0.9.0-beta.1',
    status: 'pending', signature: 'unsigned beta', byteSize: 220640505,
    sha256: '88EBD5978CEDDB18D0084577AAFC42EDF6AD04A6FF1A4AFACC8FA0153148C2CC',
    warning: 'The verified installer exists locally, but its public release URL is not published yet. SmartScreen may warn when it becomes available.'
  },
  {
    platform: 'macOS', architecture: 'ARM64 · Apple silicon', filename: 'Deckastra-0.9.0-beta.1-mac-arm64.dmg', version: '0.9.0-beta.1',
    status: 'available', signature: 'unsigned beta',
    url: 'https://storage.googleapis.com/deckastra-installer/beta-0.9/mac-os/Deckastra-0.9.0-beta.1-mac-arm64.dmg',
    byteSize: 203213219, sha256: '9312FE790F38A405862FDFC2059D0AC3389B05FE10341E462146190B473A800E',
    releaseDate: '17 October 2026',
    warning: 'Unsigned beta. macOS may require approval in System Settings → Privacy & Security before the app can open.'
  }
]
