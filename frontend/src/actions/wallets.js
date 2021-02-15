import axiosInstance from '../axios'

import {
    GET_WALLETS_SUCCESS,
    GET_WALLETS_FAIL,
    GET_BALANCE_SUCCESS,
    GET_BALANCE_FAIL
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

export const getBalance = () => dispatch => {
    axiosInstance.get('wallets/balance/')
        .then(res => {
            dispatch({
                type: GET_BALANCE_SUCCESS,
                payload: res.data
            })
        })
        .catch(err => {
            dispatch(returnErrors(err.response, 'GET_BALANCE_FAIL'))
            dispatch({
                type: GET_BALANCE_FAIL
            })
        })
}

export const removeWallet = (id) => dispatch => {
    axiosInstance.delete(`wallets/${id}`)
        .then(() => {
            dispatch({
                type: REMOVE_WALLET_SUCCESS
            })
        })
        .catch(err => {
            dispatch(returnErrors(err.response, 'GET_BALANCE_FAIL'))
            dispatch({
                type: REMOVE_WALLET_FAIL
            })
        })
}