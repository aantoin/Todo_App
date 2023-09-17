<template>
  <div>
    <ul v-if="checklistStore.checklists">
      <li v-for="checklist in checklistStore.checklists" :key="checklist.id" @click="activateChecklist(checklist.id)"
        class="border-b-2 border-layout-border hover:bg-layout-border cursor-pointer">
        {{ checklist.name }}
      </li>
    </ul>
    <div @click="createChecklist" class="border-b-2 border-layout-border hover:bg-layout-border cursor-pointer">+ New
      Checklist</div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useChecklistStore } from '@/stores/checklists'
import { useRouter } from 'vue-router'

const checklistStore = useChecklistStore()
const router = useRouter()

onMounted(() => {
  checklistStore.fetchChecklists()
})

const createChecklist = () => {
  router.push({ name: 'new_checklist' })
}
const activateChecklist = (id: string) => {
  router.push({ name: 'checklist_detail', params: { id: id } })
}
</script>

<style scoped></style>
@/stores/checklists
