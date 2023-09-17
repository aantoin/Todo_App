<template>
  <div class="h-full">
    <div class="w-full h-full flex md:hidden">
      <span class="inline-block flex-grow"></span>
      <button class="flex-grow-0 h-full p-2 hover:bg-button-hover" @click="toggleMobileMenu">
        =
      </button>
    </div>
    <nav
      class="fixed z-10 right-0 max-w-screen-sm border-nav-mobile-border border-l-2 border-b-2 shadow-black drop-shadow-md md:border-layout-border md:block md:static md:max-w-full md:h-full md:border-l-0 md:border-b-0"
      :class="{ 'left-full': !mobileMenuActive }">
      <RouterLink v-for="item in props.menuItems" :key="item.to" :to="{ name: item.to }"
        class="block p-2 bg-nav-item hover:bg-nav-item-hover md:h-full md:inline-block md:p-2"
        @click="deactivateMobileMenu">{{ item.text }}
      </RouterLink>
    </nav>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

interface MenuItem {
  to: string,
  text: string,
}
const props = defineProps<{
  menuItems: MenuItem[],
}>()

const mobileMenuActive = ref(false)
const toggleMobileMenu = () => {
  mobileMenuActive.value = !mobileMenuActive.value
}
const deactivateMobileMenu = () => {
  mobileMenuActive.value = false
}
</script>

<style scoped></style>
