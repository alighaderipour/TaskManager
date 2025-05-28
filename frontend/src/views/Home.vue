<script setup lang="ts">

</script>

<template>
<router-link to="/login" custom v-slot="{ navigate }">
    <button @click="navigate" role="link">
      Login Button
    </button>
  </router-link>
</template>

<style scoped>

</style>