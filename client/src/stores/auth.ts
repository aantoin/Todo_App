//import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { api } from '@/api'

export const useAuthStore = defineStore('auth', () => {
  /*const count = ref(0)
  const doubleCount = computed(() => count.value * 2)*/
  function logout() {
    return api.post('auth/logout/', {})
  }
  function signup(email: string, password1: string, password2: string) {
    return api.post('auth/registration/', {
      email: email,
      password1: password1,
      password2: password2
    })
  }
  function login(email: string, password: string) {
    return api.post('auth/login/', {
      email: email,
      password: password
    })
  }
  function resend_verification_email(email: string) {
    return api.post('auth/registration/resend-email/', {
      email: email
    })
  }
  async function createGuestAccount() {
    const email = "guest-" + crypto.randomUUID() + "@test.com"
    const password = crypto.randomUUID()
    const signupResponse = await signup(email, password, password)
    if (signupResponse.status == 201) {
      const loginResponse = await login(email, password);
      return loginResponse.status == 200;
    }
    return false;
  }
  return { logout, signup, login, resend_verification_email,createGuestAccount }
})
