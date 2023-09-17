<template>
  <NavBar :menu-items="menuItems" />
</template>

<script setup lang="ts">
import NavBar from '../NavBar.vue';

const menuItems = [
  { to: 'dashboard', text: 'Home' },
  { to: 'signout', text: 'Sign out' }
]
</script>

<style scoped></style>
