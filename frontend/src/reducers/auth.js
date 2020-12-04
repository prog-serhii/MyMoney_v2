import * as actionTypes from '../actions/types';

const initialState = {
    access: localStorage.getItem('access'),
    refresh: localStorage.getItem('refresh'),
    isAuthenticated: null,
    user: null
};

export default function auth(state = initialState, action) {
    const { type, payload } = action;

    switch (type) {
        case actionTypes.LOGIN_SUCCESS:
            localStorage.setItem('access', payload.access);
            return {
                ...state,
                access: payload.access,
                refresh: payload.refresh,
                isAuthenticated: true
            }
        case actionTypes.LOGIN_FAIL:
        case actionTypes.LOGOUT:
            localStorage.removeItem('access');
            localStorage.removeItem('refresh');
            return {
                ...state,
                access: null,
                refresh: null,
                user: null,
                isAuthenticated: false
            }
        case actionTypes.LOAD_USER_SUCCESS:
            return {
                ...state,
                user: payload
            }
        case actionTypes.LOAD_USER_FAIL:
            return {
                ...state,
                user: null
            }
        case actionTypes.AUTHENTICATED_SUCCESS:
            return {
                ...state,
                isAuthenticated: true
            }
        case actionTypes.AUTHENTICATED_FAIL:
            return {
                ...state,
                isAuthenticated: false
            }
        case actionTypes.PASSWORD_RESET_SUCCESS:
        case actionTypes.PASSWORD_RESET_FAIL:
        case actionTypes.PASSWORD_RESET_CONFIRM_SUCCESS:
        case actionTypes.PASSWORD_RESET_CONFIRM_FAIL:
            return {
                ...state
            }
        default:
            return state
    }
}