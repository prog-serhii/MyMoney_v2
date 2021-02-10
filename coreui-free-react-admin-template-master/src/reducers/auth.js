import {
  USER_LOADED_SUCCESS,
  USER_LOADED_FAIL,
  LOGIN_FAIL,
  LOGIN_SUCCESS,
  AUTHENTICATED_SUCCESS,
  AUTHENTICATED_FAIL,
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  LOGOUT
} from '../actions/types'


const initialState = {
  accessToken: localStorage.getItem('accessToken'),
  refreshToken: localStorage.getItem('refreshToken'),
  isAuthenticated: null,
  isRegistered: null,
  user: null,
}

export default function (state = initialState, action) {
  switch (action.type) {

    case AUTHENTICATED_SUCCESS:
      return {
        ...state,
        isAuthenticated: true
      }

    case USER_LOADED_SUCCESS:
      return {
        ...state,
        isAuthenticated: true,
        user: action.payload
      }

    case LOGIN_SUCCESS:
      localStorage.setItem('accessToken', action.payload.access)
      localStorage.setItem('refreshToken', action.payload.refresh)
      return {
        ...state,
        accessToken: action.payload.access,
        refreshToken: action.payload.refresh,
        isAuthenticated: true
      }

    case REGISTER_SUCCESS:
      return {
        ...state,
        accessToken: null,
        refreshToken: null,
        user: action.payload,
        isAuthenticated: false,
        isRegistered: true
      }

    case USER_LOADED_FAIL:
      return {
        ...state,
        isAuthenticated: false,
        user: null
      }

    case AUTHENTICATED_FAIL:
    case REGISTER_FAIL:
    case LOGIN_FAIL:
    case LOGOUT:
      localStorage.removeItem('accessToken')
      localStorage.removeItem('refreshToken')
      return {
        ...state,
        accessToken: null,
        refreshToken: null,
        user: null,
        isAuthenticated: false,
        isRegistered: false
      }

    default:
      return state
  }
}