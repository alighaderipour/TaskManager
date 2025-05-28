import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore('user', {
  state: () => ({
    userId: null
  }),
  actions: {
    async login(username, password) {
      const res = await axios.post('http://localhost:5000/api/auth/login', { username, password })
      this.userId = res.data.user_id
    }
  }
})
