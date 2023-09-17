<template>
  <div class="bg-white flex flex-col items-center w-full">
    <div class="bg-white p-2 flex flex-col items-center max-w-[600px]">
      <div class="inline-block py-2 text-4xl">Todo App</div>
      <div class="inline-block py-2 text-xl text-center">A simple app for creating checklists full of tasks, groceries, or
        whatever
        you need to remember.</div>
      <div class="inline-block py-2 text-4xl">To get started:</div>
      <div class="inline-block py-2 text-xl text-center">
        <div class="inline-block px-2"><button @click="routeToSignup"
            class="px-4 py-2 rounded-lg bg-button hover:bg-button-hover shadow-sm shadow-black">Sign
            up</button></div>
        <div class="inline-block px-2"><button @click="routeToLogin"
            class="px-4 py-2 rounded-lg bg-button hover:bg-button-hover shadow-sm shadow-black">Log
            in</button></div>
        <div class="inline-block px-2"><button @click="loginAsGuest"
            class="px-4 py-2 rounded-lg bg-button hover:bg-button-hover shadow-sm shadow-black">Guest Login</button></div>
        <div v-if="guestAccountError">Error creating guest account</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const router = useRouter()
const authStore = useAuthStore();
const guestAccountError = ref(false);

const routeToSignup = () => router.push({ name: "signup" });
const routeToLogin = () => router.push({ name: "login" });
const loginAsGuest = () => {
  authStore.createGuestAccount().then(success => {
    if (success) router.push({ name: "dashboard" });
    else guestAccountError.value = true;
  })
};
</script>

<style scoped></style>
