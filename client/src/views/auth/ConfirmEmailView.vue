<template>
  <div>
    {{ route.params.key }}
  </div>
</template>

<script setup lang="ts">
import { onBeforeMount } from 'vue'
import { useRoute } from 'vue-router'
import { api } from '@/api'
const route = useRoute()
onBeforeMount(() => {
  api
    .post('auth/registration/verify-email/', {
      key: route.params.key
    })
    .then(() => {})
    .catch(() => {})
})
</script>

<style scoped></style>
