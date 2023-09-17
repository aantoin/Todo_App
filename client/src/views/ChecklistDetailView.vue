<template>
  <div>
    <div v-if="checklist" class="grid grid-cols-[1fr_min-content] pb-2 w-full">
      <div class="text-2xl min-w-0 pr-2">
        <h1 class="overflow-hidden">{{ checklist.name }}</h1>
      </div>
      <button @click="deleteChecklist"
        class="bg-danger text-danger-text hover:bg-danger-hover rounded-md px-2 py-1">Delete</button>
    </div>
    <div>
      <div v-if="checklist">
        <ChecklistItemList :checklist="checklist" :index="0" />
      </div>
    </div>
    <div>
      <span class="block pb-2">
        <span class="flex flex-nowrap items-center p-2 bg-checklist-item rounded-lg">
          <input type="text" placeholder="Add Item..." class="w-full outline-none" v-model="newItem"
            @keyup.enter="addItem" />
        </span>
      </span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref, } from 'vue';
import { onBeforeRouteUpdate, useRoute, useRouter } from 'vue-router';
import { useChecklistStore } from '@/stores/checklists';
import type { ChecklistItem } from '@/stores/checklists';
import ChecklistItemList from '@/components/ChecklistItemList.vue';

const checklistStore = useChecklistStore();

const route = useRoute()
const router = useRouter()

const newItem = ref("");

type NestedItems = (Partial<ChecklistItem> & { children: ChecklistItem[] })[]
const nestItems = (nested_items: NestedItems, checklist_items: ChecklistItem[], start = 0) => {
  while (checklist.value && start > 0 && start < checklist_items.length) {
    nestedItems.value.push({ ...checklist.value.items[start], ...{ children: [] } });
  }
}
const nestedItems = computed(() => {
  const items = [] as NestedItems;
  if (!checklist.value) return items as NestedItems;
  nestItems(items, checklist.value.items);
  return items;
})
const checklist = computed(() => {
  return checklistStore.activeChecklist;
})
const deleteChecklist = () => {
  checklistStore.deleteChecklist(checklistStore.activeChecklistID)
  router.push({ name: 'dashboard' });
}
const addItem = () => {
  if (checklist.value) {
    checklistStore.createChecklistItem(checklist.value.id, { content: newItem.value }).then(() => {
      newItem.value = "";
      updateItems();
    });
  }
}
const updateItems = () => {
  checklistStore.fetchChecklistItems(checklistStore.activeChecklistID).then(response => {
    const items = response.data as ChecklistItem[];
    items.sort((a, b) => a.order_left - b.order_left);
    checklistStore.setChecklistItems(checklistStore.activeChecklistID, items);
  });
}
const initComponent = (new_checklist_id: string) => {
  checklistStore.activeChecklistID = new_checklist_id;
  updateItems();
}

onMounted(() => {
  initComponent(route.params['id'] as string);
})
onBeforeRouteUpdate((to, from) => {
  if (to.params.id != from.params.id) {
    initComponent(to.params.id as string);
  }
})

</script>

<style scoped></style>
