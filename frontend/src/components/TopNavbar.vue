<template>
  <header class="bg-white shadow-md sticky top-0 z-40">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <router-link to="/tasks" class="flex-shrink-0">
            <span class="text-xl font-semibold text-slate-700 hover:text-sky-600 transition-colors">Dashboard</span>
          </router-link>
        </div>

        <div class="flex items-center space-x-4 md:space-x-6">
          <nav class="hidden md:flex space-x-4">
            <router-link
              to="/reports"
              class="px-3 py-2 rounded-md text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900 transition-colors"
              active-class="bg-slate-100 text-sky-600"
            >
              Reports
            </router-link>
            <router-link
              to="/settings"
              class="px-3 py-2 rounded-md text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900 transition-colors"
              active-class="bg-slate-100 text-sky-600"
            >
              Settings
            </router-link>
            <router-link
              to="/help-center"
              class="px-3 py-2 rounded-md text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900 transition-colors"
              active-class="bg-slate-100 text-sky-600"
            >
              Help
            </router-link>
          </nav>

          <div class="relative">
            <button
              @click="toggleUserMenu"
              type="button"
              class="flex items-center text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-sky-500"
              id="user-menu-button"
              aria-expanded="false"
              aria-haspopup="true"
            >
              <span class="sr-only">Open user menu</span>
              <div class="h-8 w-8 rounded-full bg-slate-300 flex items-center justify-center text-slate-600 font-semibold">
                JD </div>
              <span class="hidden ml-2 text-sm font-medium text-slate-700 md:block">John Doe</span>
              <svg class="hidden ml-1 h-5 w-5 text-slate-500 md:block" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
            </button>

            <transition
              enter-active-class="transition ease-out duration-100"
              enter-from-class="transform opacity-0 scale-95"
              enter-to-class="transform opacity-100 scale-100"
              leave-active-class="transition ease-in duration-75"
              leave-from-class="transform opacity-100 scale-100"
              leave-to-class="transform opacity-0 scale-95"
            >
              <div
                v-if="isUserMenuOpen"
                class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5 focus:outline-none z-50"
                role="menu"
                aria-orientation="vertical"
                aria-labelledby="user-menu-button"
                tabindex="-1"
              >
                <router-link
                  to="/profile"
                  class="block px-4 py-2 text-sm text-slate-700 hover:bg-slate-100"
                  role="menuitem"
                  tabindex="-1"
                  id="user-menu-item-0"
                  @click="closeUserMenu"
                >
                  Your Profile
                </router-link>
                <button
                  @click="handleLogout"
                  class="block w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-100"
                  role="menuitem"
                  tabindex="-1"
                  id="user-menu-item-1"
                >
                  Sign out
                </button>
              </div>
            </transition>
          </div>

          <div class="md:hidden">
            <button @click="toggleMobileMenu" class="p-2 rounded-md text-slate-500 hover:text-slate-700 hover:bg-slate-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-sky-500">
              <span class="sr-only">Open main menu</span>
              <svg v-if="!isMobileMenuOpen" class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
              <svg v-else class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
          </div>

        </div>
      </div>

      <div v-if="isMobileMenuOpen" class="md:hidden border-t border-slate-200" id="mobile-menu">
        <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
          <router-link to="/reports" class="block px-3 py-2 rounded-md text-base font-medium text-slate-700 hover:bg-slate-100 hover:text-sky-600" active-class="bg-sky-50 text-sky-600" @click="closeMobileMenu">Reports</router-link>
          <router-link to="/settings" class="block px-3 py-2 rounded-md text-base font-medium text-slate-700 hover:bg-slate-100 hover:text-sky-600" active-class="bg-sky-50 text-sky-600" @click="closeMobileMenu">Settings</router-link>
          <router-link to="/help-center" class="block px-3 py-2 rounded-md text-base font-medium text-slate-700 hover:bg-slate-100 hover:text-sky-600" active-class="bg-sky-50 text-sky-600" @click="closeMobileMenu">Help</router-link>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'TopNavbar',
  data() {
    return {
      isUserMenuOpen: false,
      isMobileMenuOpen: false,
    };
  },
  methods: {
    toggleUserMenu() {
      this.isUserMenuOpen = !this.isUserMenuOpen;
    },
    closeUserMenu() {
      this.isUserMenuOpen = false;
    },
    toggleMobileMenu() {
      this.isMobileMenuOpen = !this.isMobileMenuOpen;
    },
    closeMobileMenu() {
      this.isMobileMenuOpen = false;
    },
    handleLogout() {
      this.closeUserMenu();
      // Implement your logout logic here
      // For example, clearing local storage, calling an API, then redirecting
      console.log("Logout action triggered");
      // Example: localStorage.removeItem('authToken');
      this.$router.push('/login'); // Redirect to login page
    }
  },
  mounted() {
    // Optional: Close user menu if clicked outside
    const closeOnClickOutside = (event) => {
      if (this.isUserMenuOpen && !this.$el.contains(event.target)) {
        this.isUserMenuOpen = false;
      }
    };
    document.addEventListener('click', closeOnClickOutside);
    this.$on('hook:beforeDestroy', () => {
      document.removeEventListener('click', closeOnClickOutside);
    });
  }
};
</script>

<style scoped>
/* Add any specific scoped styles if Tailwind classes are not sufficient */
/* For example, ensuring the sticky header works well with the overall layout */
header {
  /* If your SideNavbar has a specific width, you might need to adjust the
     left margin or width of the TopNavbar if it's not full-width within its container.
     However, the current Tasks.vue layout should handle this correctly. */
}
</style>
