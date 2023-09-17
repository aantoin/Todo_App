<template>
  <NavBar :menu-items="menuItems" />
</template>

<script setup lang="ts">
import NavBar from '../NavBar.vue';


const menuItems = [
  { to: 'home', text: 'Home' },
  { to: 'signup', text: 'Sign Up' },
  { to: 'login', text: 'Log In' },
]
</script>

<style scoped></style>
