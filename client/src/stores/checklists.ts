import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { api } from '@/api'

export interface ChecklistItemForm{
  content: string
}
export interface ChecklistItem {
  id: string
  checklist: string
  content: string
  completed: boolean
  order_left: number
  order_right: number
}
export interface ChecklistForm {
  name: string
}
export interface Checklist {
  id: string
  name: string
  order: number
  item_complete_action: string
  hide_completed: boolean
  hide_until_due: boolean
  items: ChecklistItem[]
}

export const useChecklistStore = defineStore('checklists', () => {
  const checklists = ref<Checklist[]>([]);
  const activeChecklistID = ref("");
  const activeChecklist = computed(() => {
    if (!activeChecklistID.value) return null;
    const checklist = checklists.value.find(element => element.id == activeChecklistID.value);
    if (checklist == undefined) return null;
    return checklist;
  })
  function resetLocalData() {
    checklists.value = [];
  }
  function fetchChecklists() {
    api.get<Checklist[]>('checklists/').then((response) => {
      checklists.value = response.data
    })
  }
  function createChecklist(checklist: ChecklistForm) {
    return api
      .post('checklists/', {
        ...checklist
      })
  }
  function appendChecklist(checklist: Checklist) {
    checklists.value.push(checklist)
  }
  function deleteChecklist(id: string) {
    api
      .delete('checklists/' + id + '/')
      .then((response) => {
        if (response.status === 204) {
          checklists.value = checklists.value.filter((x) => x.id != id)
        } else {
          console.log('failed to delete ' + id, response.status)
        }
      })
      .catch((error) => {
        console.log('failed to delete ' + id, error.response.status)
      })
  }
  function setChecklistItems(checklist_id: string, items: ChecklistItem[]) {
    checklists.value.filter(x => x.id == checklist_id).forEach(x => {
      x.items = items
    })
  }
  function fetchChecklistItems(checklist_id: string) {
    return api.get('checklists/' + checklist_id + '/items/')
  }
  function createChecklistItem(checklist_id: string, item: ChecklistItemForm) {
    return api.post('checklists/' + checklist_id + '/items/', item)
  }
  function deleteChecklistItem(checklist_id: string, item_id: string) {
    return api.delete('checklists/' + checklist_id + '/items/' + item_id + '/');
  }
  function setChecklistItemCompletion(checklist_id: string, item_id: string, value: boolean) {
    return api.patch('checklists/'+ checklist_id + '/items/' + item_id + '/', {completed:value})
  }
  return {
    checklists,
    activeChecklistID,
    activeChecklist,
    resetLocalData,
    fetchChecklists,
    createChecklist,
    appendChecklist,
    deleteChecklist,
    setChecklistItems,
    createChecklistItem,
    fetchChecklistItems,
    deleteChecklistItem,
    setChecklistItemCompletion,
  }
})
