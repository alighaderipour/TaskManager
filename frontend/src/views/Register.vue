<template>
  <div class="flex flex-col items-center justify-center h-screen bg-gray-100">
    <div class="bg-white p-8 rounded-xl shadow-md w-full max-w-md">
      <h2 class="text-2xl font-semibold mb-6 text-center">Register</h2>
      <form @submit.prevent="register">
        <input v-model="username" type="text" placeholder="Username" class="input mb-4" required />
        <input v-model="password" type="password" placeholder="Password" class="input mb-4" required />
        <button type="submit" class="btn w-full">Register</button>
      </form>
      <p class="mt-4 text-center">
        Already have an account?
        <router-link to="/login" class="text-blue-600 underline">Login here</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const router = useRouter()

const register = async () => {
  try {
    await axios.post('http://127.0.0.1:5000/register', {
      username: username.value,
      password: password.value,
    })
    alert('Registration successful! Redirecting to login...')
    router.push('/login')
  } catch (error) {
    alert(error.response?.data?.message || 'Registration failed')
  }
}
</script>

<style scoped>
.input {
  @apply w-full px-4 py-2 border rounded-md;
}
.btn {
  @apply bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700;
}
</style>
