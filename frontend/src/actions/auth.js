import axios from 'axios';

import * as actionTypes from '../actions/types';


const API_URL = 'http://localhost:8000/api'

export const checkAuthenticated = () => async dispatch => {
    if (localStorage.getItem('access')) {
        const config = {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        };

        const body = JSON.stringify({ token: localStorage.getItem('access') });

        try {
            const res = await axios.post(`${API_URL}/auth/jwt/verify/`, body, config)

            if (res.data.code !== 'token_not_valid') {
                dispatch({
                    type: actionTypes.AUTHENTICATED_SUCCESS
                });
            } else {
                dispatch({
                    type: actionTypes.AUTHENTICATED_FAIL
                });
            }
        } catch (err) {
            dispatch({
                type: actionTypes.AUTHENTICATED_FAIL
            });
        }
    } else {
        dispatch({
            type: actionTypes.AUTHENTICATED_FAIL
        });
    }
};

export const load_user = () => async dispatch => {
    if (localStorage.getItem('access')) {
        const config = {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `JWT ${localStorage.getItem('access')}`,
                'Accept': 'application/json'
            }
        };

        try {
            const res = await axios.get(`${API_URL}/auth/users/me/`, config);

            dispatch({
                type: actionTypes.LOAD_USER_SUCCESS,
                payload: res.data
            });
        } catch (err) {
            dispatch({
                type: actionTypes.LOAD_USER_FAIL
            });
        }

    } else {
        dispatch({
            type: actionTypes.LOAD_USER_FAIL
        });
    }
};

export const login = (email, password) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const body = JSON.stringify({ email, password });

    try {
        const res = await axios.post(`${API_URL}/auth/jwt/create/`, body, config);

        dispatch({
            type: actionTypes.LOGIN_SUCCESS,
            payload: res.data
        });

        dispatch(load_user());
    } catch (err) {
        dispatch({
            type: actionTypes.LOGIN_FAIL
        });
    }
};

export const logout = () => dispatch => {
    dispatch({
        type: actionTypes.LOGOUT
    });
};

export const reset_password = (email) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json',
        }
    };

    const body = JSON.stringify({ email });

    try {
        await axios.post(`${API_URL}/auth/users/reset_password/`, body, config);

        dispatch({
            type: actionTypes.PASSWORD_RESET_SUCCESS
        });
    } catch (err) {
        dispatch({
            type: actionTypes.PASSWORD_RESET_FAIL
        })
    }
};

export const reset_password_confirm = (uid, token, new_password, re_new_password) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json',
        }
    };

    const body = JSON.stringify({ uid, token, new_password, re_new_password });

    try {
        await axios.post(`${API_URL}/auth/users/reset_password_confirm/`, body, config);

        dispatch({
            type: actionTypes.PASSWORD_RESET_CONFIRM_SUCCESS
        });
    } catch (err) {
        dispatch({
            type: actionTypes.PASSWORD_RESET_CONFIRM_FAIL
        })
    }
}