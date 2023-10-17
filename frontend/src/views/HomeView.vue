<script setup lang="ts">
import { onMounted, ref } from "vue";
import axios from "axios";

// Scripts for the component
const backendMessage = ref("");

onMounted(() => {
  axios
    .get("http://127.0.0.1:5000/sampledata")
    .then((response) => {
      backendMessage.value = response.data;
    })
    .catch((error) => {
      backendMessage.value = error.message;
    });
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
