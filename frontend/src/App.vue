<script>

import TopNavbar from "@/components/TopNavbar.vue";

export default {
    name: '',
  components: {Navbar: TopNavbar},
    data() {
        return {
        }
    }
}
</script>

<template>
  <div id="app">

    <router-view />
  </div>
</template>

<style>
</style>