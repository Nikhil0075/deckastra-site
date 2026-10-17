<script setup lang="ts">
defineProps<{ items: Array<{ value: string; label: string }> }>()
</script>

<template><div class="proof-metrics"><div v-for="item in items" :key="item.label"><strong>{{ item.value }}</strong><span>{{ item.label }}</span></div></div></template>
