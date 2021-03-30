import axiosInstance from '../axios'

import {
    USER_LOADED_SUCCESS,
    USER_LOADED_FAIL,
    LOGIN_SUCCESS,
    LOGIN_FAIL,
    AUTHENTICATED_SUCCESS,
    AUTHENTICATED_FAIL,
    REGISTER_SUCCESS,
    REGISTER_FAIL,
    LOGOUT
} from './types'
import { returnErrors } from './errors'

// Load user
// export const loadUser = () => dispatch => {

//     axiosInstance.get('auth/users/me/')
//         .then(res => {
//             dispatch({
//                 type: USER_LOADED_SUCCESS,
//                 payload: res.data
//             })
//         })
//         .catch(err => {
//             //dispatch(returnErrors(err.response.data, err.response.status))
//             dispatch({
//                 type: USER_LOADED_FAIL,
//             })
//         })
// }

// Login user
export const login = (email, password) => dispatch => {

    // Request body
    const body = JSON.stringify({ email, password })

    // POST request to create a access token
    axiosInstance.post('auth/jwt/create/', body)
        .then(res => {
            dispatch({
                type: LOGIN_SUCCESS,
                payload: res.data
            })
            axiosInstance.defaults.headers['Authorization'] = 
                'JWT ' + res.data.access
        })
        .catch(err => {
            dispatch(returnErrors(err.response, 'LOGIN_FAIL'))
            dispatch({
                type: LOGIN_FAIL,
            })
        })
}

// Check if user is authenticated
export const checkAuthenticated = () => dispatch => {
    const body = JSON.stringify({ token: localStorage.getItem('accessToken') })

    axiosInstance.post('/auth/jwt/verify/', body)
        .then(res => {
            dispatch({
                type: AUTHENTICATED_SUCCESS
            })
        })
        .catch(err => {
            dispatch(returnErrors(err.response, 'AUTHENTICATED_FAIL'))
            dispatch({
                type: AUTHENTICATED_FAIL
            })
        })

}

// Logout user
export const logout = () => dispatch => {

    dispatch({
        type: LOGOUT
    })
}

// Register user
export const register = ({ name, email, password, re_password }) => dispatch => {

    const body = JSON.stringify({ name, email, password, re_password })

    axiosInstance
        .post('auth/users/', body)
        .then(res => {
            dispatch({
                type: REGISTER_SUCCESS,
                payload: res.data
            })
        })
        .catch(err => {
            dispatch(returnErrors(err.response, 'REGISTER_FAIL'))
            dispatch({
                type: REGISTER_FAIL
            })
        })
}