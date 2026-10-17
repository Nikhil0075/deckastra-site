<script setup lang="ts">
import { ref } from 'vue'
const props = defineProps<{ title: string; prompt: string }>()
const copied = ref(false)
async function copy() {
  let copiedText = false
  try {
    await navigator.clipboard.writeText(props.prompt)
    copiedText = true
  } catch {
    const textarea = document.createElement('textarea')
    textarea.value = props.prompt
    textarea.style.position = 'fixed'
    textarea.style.opacity = '0'
    document.body.appendChild(textarea)
    textarea.select()
    copiedText = document.execCommand('copy')
    textarea.remove()
  }
  if (!copiedText) return
  copied.value = true
  window.setTimeout(() => { copied.value = false }, 3000)
}
</script>

<template><div class="copy-prompt"><div><strong>{{ title }}</strong><p>{{ prompt }}</p></div><button type="button" @click="copy" :aria-label="`Copy ${title} prompt`">{{ copied ? 'Copied' : 'Copy' }}</button></div></template>
