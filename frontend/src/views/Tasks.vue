<template>
  <div class="flex h-screen bg-slate-100">
    <SideNavbar />

    <div class="flex-1 flex flex-col overflow-hidden">
      <TopNavbar />

      <main class="flex-1 overflow-x-hidden overflow-y-auto bg-slate-100 p-6 md:p-8">
        <div class="container mx-auto">
          <div class="mb-6 md:mb-8">
            <h1 class="text-2xl md:text-3xl font-semibold text-slate-800">My Tasks</h1>
            <p class="text-slate-500 text-sm mt-1">Manage and organize your daily tasks efficiently.</p>
          </div>

          <div class="bg-white shadow-lg rounded-xl p-6 md:p-8">
            <div class="animate-pulse" v-if="loading">
              <div class="h-8 bg-slate-200 rounded w-1/3 mb-4"></div>
              <div class="space-y-3">
                <div class="h-4 bg-slate-200 rounded w-full"></div>
                <div class="h-4 bg-slate-200 rounded w-5/6"></div>
                <div class="h-4 bg-slate-200 rounded w-3/4"></div>
              </div>
            </div>

            <div v-else>
              <div class="space-y-4">
                <div v-for="task in tasks" :key="task.id" class="flex items-center justify-between p-4 border border-slate-200 rounded-lg hover:shadow-md transition-shadow">
                  <div>
                    <h3 class="font-medium text-slate-700">{{ task.title }}</h3>
                    <p class="text-xs text-slate-500">{{ task.dueDate }} - <span :class="task.priority === 'High' ? 'text-red-500' : 'text-yellow-500'">{{ task.priority }} Priority</span></p>
                  </div>
                  <button class="text-sm text-sky-600 hover:text-sky-700 font-medium">View Details</button>
                </div>

                <div v-if="tasks.length === 0" class="text-center py-8">
                  <svg class="w-16 h-16 text-slate-300 mx-auto mb-4" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75"></path>
                  </svg>
                  <p class="text-slate-500">No tasks yet. Add a new task to get started!</p>
                  <button class="mt-4 px-4 py-2 bg-sky-600 hover:bg-sky-700 text-white text-sm font-medium rounded-lg shadow transition-colors">
                    Add New Task
                  </button>
                </div>
              </div>
            </div>
          </div>
          </div>
      </main>
    </div>
  </div>
</template>

<script>
// Import your Navbar components
import SideNavbar from '@/components/SideNavbar.vue'; // Adjust path if necessary
import TopNavbar from '@/components/TopNavbar.vue';   // Adjust path if necessary

export default {
  name: 'Tasks',
  components: {
    SideNavbar,
    TopNavbar
  },
  data() {
    return {
      loading: true, // Simulate loading state
      tasks: [
        // Sample task data - replace with your actual data fetching
        { id: 1, title: 'Design new homepage layout', dueDate: '2025-06-15', priority: 'High' },
        { id: 2, title: 'Develop API endpoints for user authentication', dueDate: '2025-06-20', priority: 'High' },
        { id: 3, title: 'Write documentation for the new feature', dueDate: '2025-06-25', priority: 'Medium' },
      ]
    };
  },
  mounted() {
    // Simulate fetching data
    setTimeout(() => {
      this.loading = false;
      // In a real app, you would fetch tasks here:
      // this.fetchTasks();
    }, 1500);
  },
  methods: {
    // async fetchTasks() {
    //   try {
    //     this.loading = true;
    //     // const response = await axios.get('/api/tasks');
    //     // this.tasks = response.data;
    //   } catch (error) {
    //     console.error("Failed to fetch tasks:", error);
    //     // Handle error (e.g., show a notification)
    //   } finally {
    //     this.loading = false;
    //   }
    // }
  }
};
</script>

<style scoped>
/* Scoped styles for Tasks.vue if needed */
/* For example, ensuring main content area scrolls correctly */
main {
  /* Styles for the main content scrolling area */
}
</style>
