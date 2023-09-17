<template>
  <div class="w-screen h-screen grid grid-cols-12 grid-rows-[40px] min-w-[360px]">
    <div class="col-span-12 border-b-2 border-layout-border">
      <div class="h-full">
        <DashboardNav />
      </div>
    </div>
    <div class="col-span-3 overflow-auto border-r-2 border-layout-border">
      <div class="p-2">
        <ChecklistList />
      </div>
    </div>
    <div class="col-span-9 bg-dashboard-bg">
      <div class="p-2">
        <RouterView />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import DashboardNav from '@/components/navigation/DashboardNav.vue'
import ChecklistList from '@/components/ChecklistList.vue'
</script>

<style scoped></style>
@/stores/checklists
