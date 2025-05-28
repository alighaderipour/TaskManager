<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-900 to-slate-800 text-white flex flex-col items-center justify-center p-4 overflow-hidden">
    <div class="absolute inset-0 pointer-events-none" aria-hidden="true">
      <div v-for="i in 30" :key="`particle-${i}`" class="particle" :style="particleStyle()"></div>
    </div>

    <main class="relative z-10 flex flex-col items-center text-center animate-fade-in-up">
      <div class="mb-8 p-5 bg-white/10 rounded-full shadow-2xl backdrop-blur-md">
        <svg class="w-16 h-16 text-sky-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9 17.25v1.007a3 3 0 01-.379 1.503L5.25 21M9 17.25v-4.5M9 17.25H5.25m11.25-4.5h3.75a3 3 0 013 3v1.007a3 3 0 01-1.503 2.621L16.5 21M16.5 12.75v4.5M16.5 12.75h3.75M9 12.75h7.5M9 12.75c0-1.131.895-2.056 2.006-2.121L12 10.5M9 12.75c0-2.073 1.686-3.75 3.75-3.75S16.5 10.677 16.5 12.75m0 0c0 1.131-.895 2.056-2.006 2.121L12 15.375M12 10.5c.053 0 .105.002.157.004L12 10.5m0 0c.053 0 .105.002.157.004M12 5.25a2.25 2.25 0 00-2.25 2.25s0 1.125 1.125 1.125S12 9 12 9s1.125 0 1.125-1.125S13.125 5.25 12 5.25z" />
        </svg>
      </div>

      <h1 class="text-4xl sm:text-5xl md:text-6xl font-extrabold mb-6 leading-tight">
        Welcome to <span class="text-sky-400">TaskMaster</span>
      </h1>
      <p class="text-lg sm:text-xl text-slate-300 max-w-2xl mb-10">
        Organize your life, boost your productivity, and achieve your goals with our intuitive task management platform.
        Seamlessly manage your projects and collaborate with your team.
      </p>

      <router-link
        to="/login"
        class="px-8 py-3 bg-sky-500 hover:bg-sky-600 text-white font-semibold rounded-lg text-lg shadow-lg transform transition-all duration-300 hover:scale-105 focus:outline-none focus:ring-2 focus:ring-sky-400 focus:ring-opacity-75"
      >
        Get Started
      </router-link>

      <div class="mt-16 text-sm text-slate-400">
        <p>&copy; {{ new Date().getFullYear() }} TaskMaster Inc. All rights reserved.</p>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'Home',
  methods: {
    // For the optional particle background
    particleStyle() {
      const size = Math.random() * 5 + 2; // Particle size between 2px and 7px
      return {
        width: `${size}px`,
        height: `${size}px`,
        left: `${Math.random() * 100}%`,
        top: `${Math.random() * 100}%`,
        animationDuration: `${Math.random() * 10 + 10}s`, // Duration between 10s and 20s
        animationDelay: `${Math.random() * 5}s`, // Delay up to 5s
        opacity: Math.random() * 0.3 + 0.1, // Opacity between 0.1 and 0.4
      };
    }
  }
};
</script>

<style scoped>
/* Main fade-in animation for content */
@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.animate-fade-in-up {
  animation: fade-in-up 0.8s ease-out forwards;
}

/* Particle animation (Optional) */
@keyframes particle-float {
  0% {
    transform: translateY(0px) translateX(0px) scale(1);
  }
  50% {
    transform: translateY(-20px) translateX(10px) scale(1.1);
  }
  100% {
    transform: translateY(0px) translateX(0px) scale(1);
  }
}

.particle {
  position: absolute;
  background-color: rgba(165, 243, 252, 0.3); /* Light sky blue, semi-transparent */
  border-radius: 50%;
  animation-name: particle-float;
  animation-timing-function: ease-in-out;
  animation-iteration-count: infinite;
  box-shadow: 0 0 10px rgba(165, 243, 252, 0.2), 0 0 20px rgba(165, 243, 252, 0.1);
}

/* Ensuring the router-link (<a> tag) behaves as expected with Tailwind */
a {
  @apply text-sky-400 hover:text-sky-300 transition-colors duration-200;
}
.router-link-exact-active { /* Example if you want to style active links differently */
  /* @apply text-sky-300; */
}

/* Custom button styling if needed beyond Tailwind classes */
.btn-primary {
  @apply px-8 py-3 bg-sky-500 hover:bg-sky-600 text-white font-semibold rounded-lg text-lg shadow-lg;
  @apply transform transition-all duration-300 hover:scale-105;
  @apply focus:outline-none focus:ring-2 focus:ring-sky-400 focus:ring-opacity-75;
}
</style>
