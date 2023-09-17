<template>
  <div class="w-full py-4"><span class="block w-full text-center border-b-2 border-b-layout-border leading-[0em]"><span
        class="bg-white px-4">OR</span></span></div>
  <div class="p-2 inline-block"><button @click="createGuestAccount"
      class="px-4 py-2 rounded-lg bg-button hover:bg-button-hover shadow-sm shadow-black">Create a Guest
      Account</button>
  </div>
</template>

<script setup lang="ts">

import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';

const authStore = useAuthStore();

const router = useRouter();
const createGuestAccount = () => {
  authStore.createGuestAccount().then(success => {
    if (success) router.push({ name: "dashboard" });
  })
}
</script>

<style scoped></style>
