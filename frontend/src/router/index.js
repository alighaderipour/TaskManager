import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Home from '../views/Home.vue'
import Dashboard from '../views/Dashboard.vue'
import Register from '../views/Register.vue'
import Tasks from '../views/Tasks.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/login', name: 'Login', component: Login },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/Register', name: 'Register', component: Register },
  { path: '/Tasks', name: 'Tasks', component: Tasks },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
