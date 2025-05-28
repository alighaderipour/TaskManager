<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-r from-blue-50 to-indigo-100 px-4">
    <div class="w-full max-w-md bg-white shadow-xl rounded-3xl p-8 md:p-10 animate-fade-in">
      <div class="flex flex-col items-center mb-6">
        <div class="bg-indigo-100 p-3 rounded-full">
          <svg class="w-8 h-8 text-indigo-600" fill="none" stroke="currentColor" stroke-width="2"
            viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M5.121 17.804A13.937 13.937 0 0112 15c2.485 0 4.779.73 6.879 1.979M15 10a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
        </div>
        <h2 class="text-2xl md:text-3xl font-bold text-gray-800 mt-4">Welcome Back</h2>
        <p class="text-gray-500 text-sm mt-1">Please sign in to your account</p>
      </div>

      <form @submit.prevent="handleLogin" class="space-y-5">
        <div>
          <label for="username" class="block text-sm font-medium text-gray-700 mb-1">Username</label>
          <input
            type="text"
            id="username"
            v-model="username"
            placeholder="Enter your username"
            class="w-full px-4 py-2 border border-gray-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:outline-none transition"
            required
          />
        </div>

        <div>
          <label for="password" class="block text-sm font-medium text-gray-700 mb-1">Password</label>
          <input
            type="password"
            id="password"
            v-model="password"
            placeholder="••••••••"
            class="w-full px-4 py-2 border border-gray-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:outline-none transition"
            required
          />
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full py-2 px-4 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-xl transition duration-200 disabled:opacity-50"
        >
          <span v-if="!loading">Sign In</span>
          <span v-else>Signing In...</span>
        </button>
      </form>

      <!-- Feedback -->
      <div class="text-center mt-4">
        <p v-if="successMessage" class="text-green-600 text-sm">{{ successMessage }}</p>
        <p v-if="errorMessage" class="text-red-600 text-sm">{{ errorMessage }}</p>
      </div>

      <div class="mt-6 text-sm text-center text-gray-500">
        Don’t have an account?
        <router-link to="/register" class="text-indigo-600 hover:underline">Sign up</router-link>

      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      successMessage: "",
      errorMessage: "",
      loading: false,
    };
  },
  methods: {
  async handleLogin() {
    this.successMessage = "";
    this.errorMessage = "";
    this.loading = true;

    try {
      const response = await axios.post("http://127.0.0.1:5000/login", {
        username: this.username,
        password: this.password,
      });

      this.successMessage = "Login successful!";
      // Redirect to /tasks
      this.$router.push('/tasks');
    } catch (error) {
      this.errorMessage =
        error.response?.data?.error || "Login failed. Please try again.";
    } finally {
      this.loading = false;
    }
  },
},

};
</script>

<style scoped>
@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(16px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fade-in 0.5s ease-out;
}
</style>
