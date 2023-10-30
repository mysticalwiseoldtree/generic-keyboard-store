<script setup lang="ts">
// Scripts for the component

import { onMounted, ref } from 'vue'
import { Backend } from '../modules/backend'
import type { Product } from '../types/product';
import ProductCard from '../components/ProductCard.vue'

const backendObject = ref<Product>()

// Executes when the component is mounted
onMounted(async () => {
  // Get data from the backend
  backendObject.value = await Backend.get<Product>('sampleproduct')
})
</script>

<template>
  <div class="bg-red-50">
    <div class="pl-20 pt-20">
      <h1 class="text-5xl">Keyboard Store</h1>
      <h4 class="text-2xl">Keyboards of the highest quality in the entire of Asia.</h4>
    </div>
    <div class="w-fill pt-20 px-20">
      <h3 class="text-3xl pb-5">Featured</h3>
      <div>
        <ProductCard :product-obj="backendObject" />
      </div>
    </div>
    <div class="p-20">
      <h3 class="text-3xl pb-5">On shelve</h3>
      <div class="grid grid-rows-4 grid-flow-col gap-4">
        <ProductCard :product-obj="backendObject" />
        <ProductCard :product-obj="backendObject" />
        <ProductCard :product-obj="backendObject" />
        <ProductCard :product-obj="backendObject" />
        <ProductCard :product-obj="backendObject" />
        <ProductCard :product-obj="backendObject" />
        <ProductCard :product-obj="backendObject" />
        <ProductCard :product-obj="backendObject" />
        <ProductCard :product-obj="backendObject" />
        <ProductCard :product-obj="backendObject" />
        <ProductCard :product-obj="backendObject" />
        <ProductCard :product-obj="backendObject" />
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Styles for the component */
</style>
../types/interfaces
