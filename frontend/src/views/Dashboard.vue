<template>
  <div class="flex h-screen">
    <SideNavbar />
    <div class="flex-1 flex flex-col">
      <TopNavbar />
      <div class="flex-1 p-4 bg-gray-50">
        <Tasks />
      </div>
    </div>
  </div>
</template>

<script setup>
import TopNavbar from '../components/TopNavbar.vue'
import SideNavbar from '../components/SideNavbar.vue'
import Tasks from './Tasks.vue'
</script>
