<script setup lang="ts">
// Scripts for the component

import { onMounted, ref } from "vue";
import { Backend } from "../modules/backend";

const backendMessage = ref("");

// Executes when the component is mounted
onMounted(async () => {
  // Get data from the backend
  backendMessage.value = await Backend.get("sampledata");
});
</script>

<template>
  <div class="container">
    <h1>Home View</h1>
    <p>message from backend: {{ backendMessage }}</p>
    <button @click="$router.push('/about')">go to About page</button>
  </div>
</template>

<style scoped>
/* Styles for the component */
</style>
