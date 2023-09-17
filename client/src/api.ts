import axios from 'axios'
import router from '@/router/index'

// const BASE_URL = 'http://127.0.0.1:8000/'
const BASE_URL = 'https://www.localhost/api/'

export const api = axios.create({
  baseURL: BASE_URL,
  withCredentials: true
})

api.defaults.headers.common['Content-Type'] = 'application/json'

export const refreshAccessTokenFn = async () => {
  try {
    await api.post('auth/token/refresh/', {})
    return true
  } catch (error) {
    return false
  }
}
const isAuthenticationError = (status: number, code: string, detail: string) => {
  return (
    status == 403 && detail && detail.includes('Authentication credentials were not provided.') ||
    status == 403 && code && code.includes('token_not_valid')
  )
}
const logAPIError = (error:any) => {
  if (import.meta.env.DEV) {
    if (error.response) {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx
      console.log('Error Response', {
        data: error.response.data,
        status: error.response.status,
        headers: error.response.headers,
        code: error.response.data.code
      })
    } else if (error.request) {
      // The request was made but no response was received
      // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
      // http.ClientRequest in node.js
      console.log('Error Request', error.request)
    } else {
      // Something happened in setting up the request that triggered an Error
      console.log('Error Message', error.message)
    }
  }
}

api.interceptors.response.use(
  (response) => {
    return response
  },
  async (error) => {
    const errCode = error.response.data.code as string
    const detail = error.response.data.detail as string
    const status = error.response.status as number
    if (isAuthenticationError(status, errCode, detail)) {
      const originalRequest = error.config
      if (!originalRequest._retry) {
        originalRequest._retry = true
        const refresh = await refreshAccessTokenFn()
        if (refresh) return api(originalRequest)
      }
      router.push({ name: 'login' })
    }
    else {
      logAPIError(error);
    }
    return Promise.reject(error)
  }
)
