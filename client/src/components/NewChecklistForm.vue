<template>
  <div class="flex justify-center">
    <div class="bg-white flex items-center flex-col flex-nowrap w-[80%]">
      <div class="block">
        <h1 class="text-2xl text-center">New Checklist</h1>
      </div>
      <div class="p-2 inline-block w-3/4">
        <input type="text" placeholder="Name" v-model="name"
          class="border-2 border-layout-border rounded-md h-10 w-full" />
      </div>
      <div class="p-2 inline-block">
        <button type="submit" @click="createChecklist"
          class="px-4 py-2 rounded-lg bg-button hover:bg-button-hover shadow-sm shadow-black">Create</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useChecklistStore } from '@/stores/checklists'

const router = useRouter()
const checklistStore = useChecklistStore()

const name = ref('')

const createChecklist = () => {
  checklistStore.createChecklist({ name: name.value }).then(response => {
    checklistStore.appendChecklist(response.data)
    router.push({ name: 'checklist_detail', params: { id: response.data.id } })
  })
}
</script>

<style scoped></style>
