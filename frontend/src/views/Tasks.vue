<template>
  <div>
    <h2 class="text-xl font-bold mb-4">Your Tasks</h2>
    <ul>
      <li v-for="task in tasks" :key="task.id" class="p-2 border-b">
        <strong>{{ task.title }}</strong> - {{ task.description }}
        <span v-if="task.is_completed" class="text-green-600 ml-2">✓ Completed</span>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from '../store'
import axios from 'axios'

const store = useUserStore()
const tasks = ref([])

const fetchTasks = async () => {
  const res = await axios.get(`http://localhost:5000/api/tasks/${store.userId}`)
  tasks.value = res.data
}

onMounted(fetchTasks)
</script>
