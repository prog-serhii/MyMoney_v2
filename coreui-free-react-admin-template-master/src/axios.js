import axios from 'axios'

const baseURL = 'http://localhost:8000/api/'

const axiosInstance = axios.create({
    baseURL: baseURL,
    timeout: 5000,
    headers: {
        'Authorization': localStorage.getItem('accessToken')
            ? 'JWT ' + localStorage.getItem('accessToken')
            : null,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
})

export default axiosInstance