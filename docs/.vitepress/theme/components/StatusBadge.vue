<script setup lang="ts">
withDefaults(defineProps<{ tone?: 'available' | 'beta' | 'pending' }>(), { tone: 'beta' })
</script>

<template><span class="status-badge" :data-tone="tone"><slot /></span></template>
