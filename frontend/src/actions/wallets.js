import axiosInstance from '../axios'

import {
    GET_WALLETS_SUCCESS,
    GET_WALLETS_FAIL
} from './types'

import { returnErrors } from './errors'


export const getWallets = () => dispatch => {
    axiosInstance.get('wallets/')
        .then(res => {
            dispatch({
                type: GET_WALLETS_SUCCESS,
                payload: res.data
            })
        })
        .catch(err => {
            dispatch(returnErrors(err.response, 'GET_WALLETS_FAIL'))
            dispatch({
                type: GET_WALLETS_FAIL,
            })
        })
}