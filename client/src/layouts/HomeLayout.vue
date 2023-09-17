<template>
  <div class="w-screen h-screen grid grid-cols-12 grid-rows-[40px] min-w-[360px]">
    <div class="col-span-12 border-b-2 border-layout-border">
      <div class="h-full">
        <MainNavAnon />
      </div>
    </div>
    <div class="col-span-12 bg-dashboard-bg">
      <div class="p-2">
        <RouterView />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import MainNavAnon from '@/components/navigation/MainNavAnon.vue'
</script>

<style scoped></style>
