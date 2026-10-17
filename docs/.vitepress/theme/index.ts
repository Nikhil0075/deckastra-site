import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import './custom.css'
import ArchitecturePanel from './components/ArchitecturePanel.vue'
import DownloadCards from './components/DownloadCards.vue'
import EvidenceGallery from './components/EvidenceGallery.vue'
import FeatureGrid from './components/FeatureGrid.vue'
import HeroPanel from './components/HeroPanel.vue'
import ProofMetrics from './components/ProofMetrics.vue'
import CopyPrompt from './components/CopyPrompt.vue'
import StatusBadge from './components/StatusBadge.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('ArchitecturePanel', ArchitecturePanel)
    app.component('DownloadCards', DownloadCards)
    app.component('EvidenceGallery', EvidenceGallery)
    app.component('FeatureGrid', FeatureGrid)
    app.component('HeroPanel', HeroPanel)
    app.component('ProofMetrics', ProofMetrics)
    app.component('CopyPrompt', CopyPrompt)
    app.component('StatusBadge', StatusBadge)
  }
} satisfies Theme
