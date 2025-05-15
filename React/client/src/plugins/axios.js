import axios from 'axios'

if (import.meta.env.DEV) {
  axios.defaults.baseURL = 'http://localhost:8000'
}
