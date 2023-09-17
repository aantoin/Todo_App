<template>
  <div class="flex justify-center">
    <div class="bg-white flex items-center flex-col flex-nowrap w-[80%]">
      <div class="block">
        <h1 class="text-2xl text-center">Sign up</h1>
      </div>
      <div class="p-2 inline-block w-1/2"><input type="email" placeholder="Email" v-model="email"
          class="border-2 border-layout-border rounded-md h-10 w-full" /></div>
      <div class="p-2 inline-block w-1/2"><input type="password" placeholder="Password" v-model="password1"
          class="border-2 border-layout-border rounded-md h-10 w-full" /></div>
      <div class="p-2 inline-block w-1/2"><input type="password" placeholder="Repeat Password" v-model="password2"
          class="border-2 border-layout-border rounded-md h-10 w-full" /></div>
      <div class="p-2 inline-block"><button type="submit" @click="signup"
          class="px-4 py-2 rounded-lg bg-button hover:bg-button-hover shadow-sm shadow-black">Sign up</button></div>
      <GuestLoginFormAttachment />
    </div>

  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import GuestLoginFormAttachment from '../GuestLoginFormAttachment.vue';

const authStore = useAuthStore()

const email = ref('')
const password1 = ref('')
const password2 = ref('')

const signup = () => {
  authStore.signup(email.value, password1.value, password2.value)
}
</script>

<style scoped></style>
