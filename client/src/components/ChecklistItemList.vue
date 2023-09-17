<template>
  <ul v-if="checklistStore.activeChecklist">
    <li v-for="i in levelIndicies" :key="'checklist_item_' + i">
      <span class="block pb-2">
        <span class="flex flex-nowrap items-center p-2 bg-checklist-item rounded-lg">
          <input type="checkbox" @change="event => changeCompletionStatus(event, props.checklist.items[i].id)"
            v-model="checklistStore.activeChecklist.items[i].completed" />
          <span class="flex-grow px-2 overflow-hidden whitespace-nowrap">{{ props.checklist.items[i].content }}</span>
          <span class="p-2">
            <span
              class="p-1 text-danger-text bg-danger hover:bg-danger-hover cursor-pointer w-4 aspect-square leading-[0] flex items-center justify-center rounded-md"
              @click="deleteItem(props.checklist.items[i].id)">&#x00d7;</span>
          </span>
        </span>
      </span>
      <ChecklistItemList v-if="props.checklist.items[i].order_left < props.checklist.items[i].order_right - 1"
        :checklist="props.checklist" :index="i + 1" class="pl-4" />
    </li>
  </ul>
</template>

<script setup lang="ts">
import type { Checklist } from '@/stores/checklists';
import { computed } from 'vue';
import { useChecklistStore } from '@/stores/checklists';
import ChecklistItemList from '@/components/ChecklistItemList.vue';

const checklistStore = useChecklistStore();

const props = defineProps<{
  checklist: Checklist,
  index: number,
}>()

const levelIndicies = computed(() => {
  console.log(props.checklist)
  if (props.checklist && props.checklist.items) {
    let i = props.index;
    let right = -1;
    let indicies = [] as number[];
    while (i < props.checklist.items.length) {
      console.log(i, right, indicies)
      if (props.checklist.items[i].order_left == right + 1 || right == -1) {
        indicies.push(i);
        right = props.checklist.items[i].order_right;
        console.log("After push", i, right, indicies)
      }
      i++;
    }
    return indicies;
  }
  return [] as number[];
});

const updateItems = () => {
  checklistStore.fetchChecklistItems(props.checklist.id).then(response => {
    checklistStore.setChecklistItems(props.checklist.id, response.data);
  });
}
const deleteItem = (item_id: string) => {
  checklistStore.deleteChecklistItem(props.checklist.id, item_id).then(() => {
    updateItems();
  }).catch(() => {

  })
}
const changeCompletionStatus = (event: Event, id: string) => {
  if (event !== null && event.target !== null) {
    const target = event.target as HTMLInputElement;
    checklistStore.setChecklistItemCompletion(checklistStore.activeChecklistID, id, target.checked);
  }
}
</script>

<style scoped></style>
