<script setup lang="ts">
// Scripts for the component

import { onMounted, ref } from 'vue'
import { Backend } from '../modules/backend'
import { Product } from '../types/product'

const backendMessage = ref<Product>()

// Executes when the component is mounted
onMounted(async () => {
  // Get data from the backend
  backendMessage.value = await Backend.get<Product>('sampleproduct')
})
</script>

<template>
  <div class="container">
    <h1>Home View</h1>
    <div class="product-entry">
      <img :src="backendMessage?.image" alt="product image" />
      <h3>Name: {{ backendMessage?.name }}</h3>
      <h3>Category: {{ backendMessage?.category }}</h3>
      <h3>Price: {{ backendMessage?.price }}</h3>
    </div>
    <button @click="$router.push('/about')">go to About page</button>
  </div>
</template>

<style scoped>
/* Styles for the component */
</style>
../types/interfaces
