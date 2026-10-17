<script setup lang="ts">
import { downloads } from '../../data/site-data'
import StatusBadge from './StatusBadge.vue'
const mib = (bytes?: number) => bytes ? `${(bytes / 1048576).toFixed(1)} MiB` : '—'
</script>

<template>
  <div class="download-grid">
    <article v-for="item in downloads" :key="item.platform" class="download-card" :class="{ available: item.status === 'available' }">
      <div class="download-top"><span class="platform-icon" aria-hidden="true">{{ item.platform === 'Windows' ? '⊞' : item.platform === 'macOS' ? '◆' : '◎' }}</span><StatusBadge :tone="item.status === 'available' ? 'available' : 'pending'">{{ item.status === 'available' ? 'Available' : 'Pending' }}</StatusBadge></div>
      <h2>{{ item.platform }}</h2><p class="arch">{{ item.architecture }}</p>
      <dl><div><dt>Version</dt><dd>{{ item.version }}</dd></div><div><dt>Status</dt><dd>{{ item.signature }}</dd></div><div><dt>Size</dt><dd>{{ mib(item.byteSize) }}</dd></div><div v-if="item.releaseDate"><dt>Released</dt><dd>{{ item.releaseDate }}</dd></div></dl>
      <a v-if="item.url" class="button primary download-button" :href="item.url">{{ item.platform === 'Web' ? 'Open Web App' : `Download ${item.platform}` }}</a>
      <button v-else type="button" class="button disabled download-button" disabled>Not yet available</button>
      <p class="download-warning">{{ item.warning }}</p>
      <details v-if="item.sha256"><summary>Verify SHA-256</summary><code>{{ item.sha256 }}</code></details>
    </article>
  </div>
</template>
