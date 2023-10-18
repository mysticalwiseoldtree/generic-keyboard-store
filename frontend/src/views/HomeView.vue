<script setup lang="ts">
// Scripts for the component

import { onMounted, ref } from "vue";
import { Backend } from "../modules/backend";
import { Keyboard } from "../types/keyboard";

const backendMessage = ref<Keyboard>();

// Executes when the component is mounted
onMounted(async () => {
  // Get data from the backend
  backendMessage.value = await Backend.get<Keyboard>("samplekeyboard");
});
</script>

<template>
  <div class="container">
    <h1>Home View</h1>
    <div class="keyboard-entry">
      <img :src="backendMessage?.image" alt="keyboard image" />
      <h3>Name: {{ backendMessage?.name }}</h3>
      <h3>Brand: {{ backendMessage?.brand }}</h3>
      <h3>Price: {{ backendMessage?.price }}</h3>
    </div>
    <button @click="$router.push('/about')">go to About page</button>
  </div>
</template>

<style scoped>
/* Styles for the component */
</style>
../types/interfaces
