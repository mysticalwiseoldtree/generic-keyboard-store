<script setup lang="ts">
// Scripts for the component

import type { PropType } from "vue";
import type { Product } from "../types/product";

const props = defineProps({
  productObj: Object as PropType<Product>,
})
</script>

<template>
  <div class=" border-slate-400 border-4 bg-orange-100">
    <!-- HTML elements for the component -->
    <img class="w-full object-cover" :src="props.productObj?.image" />
    <div class="p-3 flex flex-col gap-2">
      <h1 class="text-xl font-semibold">{{ props.productObj?.name }}</h1>
      <h3 class=" opacity-70">{{ props.productObj?.description }}</h3>
      <p class="opacity-50 font-light">{{ props.productObj?.category }}</p>
      <div class="bg-green-100 p-2 text-center border hover:shadow-lg transition-shadow">
        <p>Purchase - S$200.00</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* CSS styles for the component */
</style>
