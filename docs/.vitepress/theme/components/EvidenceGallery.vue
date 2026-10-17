<script setup lang="ts">
import { computed, ref } from 'vue'
import { withBase } from 'vitepress'
import { evidence } from '../../data/evidence'

const categories = ['All', 'Authoring', 'Agents', 'Motion', 'Presentation', 'Languages', 'Recovery', 'Export', 'Settings'] as const
const active = ref<(typeof categories)[number]>('All')
const selected = ref<(typeof evidence)[number] | null>(null)
const visible = computed(() => active.value === 'All' ? evidence : evidence.filter(item => item.category === active.value))
</script>

<template>
  <div class="gallery-controls" role="group" aria-label="Filter evidence"><button v-for="category in categories" :key="category" type="button" :class="{ active: active === category }" @click="active = category">{{ category }}</button></div>
  <div class="evidence-grid"><button v-for="item in visible" :key="item.id" class="evidence-card" type="button" @click="selected = item"><img :src="withBase(item.image)" :alt="item.alt" loading="lazy" width="1783" height="1034"><span><strong>{{ item.title }}</strong><small>{{ item.category }} · verified {{ item.verified }}</small></span></button></div>
  <Teleport to="body"><div v-if="selected" class="lightbox" role="dialog" aria-modal="true" :aria-label="selected.title" @click.self="selected = null"><button class="lightbox-close" type="button" @click="selected = null" aria-label="Close screenshot">×</button><figure><img :src="withBase(selected.image)" :alt="selected.alt"><figcaption><strong>{{ selected.title }}</strong><span>{{ selected.caption }}</span></figcaption></figure></div></Teleport>
</template>
