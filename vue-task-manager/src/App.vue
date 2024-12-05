<template>
  <v-app>
    <!-- Main application container -->
    <router-view></router-view>
  </v-app>
</template>

<script setup>
// Using script setup for Vue 3 Composition API
defineOptions({
  name: 'App'
})
</script>

<style>
/* Global styles */
:root {
  --primary-color: #1976d2;
  --error-color: #ff5252;
}

/* Ensure the app takes full height */
html, body {
  height: 100%;
  margin: 0;
}

.v-application {
  min-height: 100vh;
}
</style>
