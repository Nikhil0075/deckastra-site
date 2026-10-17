<script setup lang="ts">
import { withBase } from 'vitepress'
</script>

<template>
  <section class="hero-panel">
    <div class="hero-copy">
      <p class="eyebrow">AI-native presentation studio</p>
      <h1>Presentations with agent speed.<br><span>Human control.</span></h1>
      <p class="hero-lede">Create structured, editable presentations manually, with an AI assistant, or through connected agents. Every connected-agent change waits for your approval.</p>
      <div class="hero-actions">
        <a class="button primary" href="https://deckastra-web-794139896808.asia-south1.run.app/">Open Web App</a>
        <a class="button secondary" :href="withBase('/download')">Download beta</a>
        <a class="text-link" :href="withBase('/product/agent-review')">See agent review →</a>
        <a class="text-link" href="https://github.com/Nikhil0075/deckastra">View on GitHub →</a>
      </div>
      <div class="hero-meta"><span>Structured .mydeck</span><span>PDF + PowerPoint</span><span>50 MCP tools</span></div>
    </div>
    <div class="hero-visual" aria-label="Deckastra application preview">
      <div class="window-chrome"><i></i><i></i><i></i><span>Deckastra</span></div>
      <img :src="withBase('/screenshots/10-proposal-review.png')" alt="Deckastra proposal review showing before and after slides" width="1783" height="1034">
      <div class="approval-chip"><span>✓</span><div><strong>You decide</strong><small>Approve or reject every agent change</small></div></div>
    </div>
  </section>
</template>
