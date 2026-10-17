<script setup lang="ts">
import { withBase } from 'vitepress'
defineProps<{ image: string; title: string; caption: string }>()
</script>

<template><figure class="architecture-panel"><img :src="withBase(image)" :alt="title"><figcaption><strong>{{ title }}</strong><span>{{ caption }}</span></figcaption></figure></template>
