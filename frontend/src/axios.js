import axios from 'axios';

const baseURL = 'http://127.0.0.1:8000/api/';

const axiosInstance = axios.create({
	baseURL: baseURL,
	timeout: 5000,
	headers: {
		Authorization: localStorage.getItem('accessToken')
			? 'JWT ' + localStorage.getItem('accessToken')
			: null,
		'Content-Type': 'application/json',
		accept: 'application/json',
	}, 
});

axiosInstance.interceptors.response.use(
	(response) => {
		return response
	},
	async function (error) {
		const originalRequest = error.config

		if (typeof error.response === 'undefined') {
			alert(
				'A server/network error occurred.'
			)
			return Promise.reject(error)
		}

		if (
			error.response.status === 401 &&
			originalRequest.url === baseURL + 'auth/jwt/refresh/'
		) {
			window.location.href = '/login/'
			return Promise.reject(error)
		}

		if (
			error.response.status === 401 &&
			error.response.statusText === 'Unauthorized'
		) {
			const refreshToken = localStorage.getItem('refreshToken')

			if (refreshToken) {
				const tokenParts = JSON.parse(atob(refreshToken.split('.')[1]));

				// exp date in token is expressed in seconds, while now() returns milliseconds:
				const now = Math.ceil(Date.now() / 1000)
				console.log(tokenParts.exp)

				if (tokenParts.exp > now) {
					return axiosInstance
						.post('/auth/jwt/refresh/', { refresh: refreshToken })
						.then((response) => {
							localStorage.setItem('accessToken', response.data.access)
							localStorage.setItem('refreshToken', response.data.refresh)

							axiosInstance.defaults.headers['Authorization'] =
								'JWT ' + response.data.access;
							originalRequest.headers['Authorization'] =
								'JWT ' + response.data.access

							return axiosInstance(originalRequest)
						})
						.catch((err) => {
							console.log(err)
						})
				} else {
					console.log('Refresh token is expired', tokenParts.exp, now)
					window.location.href = '/login/'
				}
			} else {
				console.log('Refresh token not available.')
				window.location.href = '/login/'
			}
		}

		// specific error handling done elsewhere
		return Promise.reject(error)
	}
);

export default axiosInstance