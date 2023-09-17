<template>
  <div class="flex justify-center">
    <div class="bg-white flex items-center flex-col flex-nowrap w-[80%]">
      <div class="block">
        <h1 class="text-2xl text-center">Log In</h1>
      </div>
      <div class="p-2 inline-block w-1/2"><input type="email" placeholder="Email" v-model="email"
          class="border-2 border-layout-border rounded-md h-10 w-full" /></div>
      <div class="p-2 inline-block w-1/2"><input type="password" placeholder="Password" v-model="password"
          class="border-2 border-layout-border rounded-md h-10 w-full" /></div>
      <div class="p-2 inline-block"><button type="submit" @click="login"
          class="px-4 py-2 rounded-lg bg-button hover:bg-button-hover shadow-sm shadow-black">Log In</button></div>
      <div v-if="errors" class="block">
        <div v-for="error in errors" :key="error[0]">
          {{ error[0] + ',' + error[1] }}
          <button v-if="error[1].includes('E-mail is not verified.')" @click="resend_verification_email">
            Resend
          </button>
        </div>
      </div>
      <GuestLoginFormAttachment />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { api } from '@/api'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

import GuestLoginFormAttachment from '../GuestLoginFormAttachment.vue';

const authStore = useAuthStore()

const router = useRouter()

const email = ref('')
const password = ref('')
const errors = ref<[string, any][]>([])

const login = () => {
  authStore
    .login(email.value, password.value)
    .then((response) => {
      api.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`
      router.push({ name: 'dashboard' })
    })
    .catch((e) => {
      if (e.response) {
        errors.value = []
        for (let field in e.response.data) {
          errors.value.push([field, e.response.data[field]])
          console.log(errors.value.slice(-1))
        }
      }
    })
}
const resend_verification_email = () => {
  authStore.resend_verification_email(email.value)
}
</script>

<style scoped></style>
