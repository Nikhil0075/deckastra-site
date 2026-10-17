<script setup lang="ts">
defineProps<{ items: Array<{ icon: string; title: string; text: string; link?: string }> }>()
</script>

<template>
  <div class="feature-grid">
    <component v-for="item in items" :key="item.title" :is="item.link ? 'a' : 'article'" :href="item.link" class="feature-card">
      <span class="feature-icon" aria-hidden="true">{{ item.icon }}</span>
      <h3>{{ item.title }}</h3><p>{{ item.text }}</p><span v-if="item.link" class="card-arrow">Explore →</span>
    </component>
  </div>
</template>
