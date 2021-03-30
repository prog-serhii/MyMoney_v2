import axiosInstance from '../axios'
import {
    GET_EXCHANGE_RATES,
    GET_EXCHANGE_RATES_SUCCESS,
    GET_EXCHANGE_RATES_FAIL,
    GET_BALANCE,
    GET_BALANCE_SUCCESS,
    GET_BALANCE_FAIL
} from './types'

import { returnErrors } from './errors'


export const getExchangeRates = () => dispatch => {
    dispatch({
        type: GET_EXCHANGE_RATES
    })

    axiosInstance.get('currencies/rates/')
        .then(res => {
            dispatch({
                type: GET_EXCHANGE_RATES_SUCCESS,
                payload: res.data
            })
        })
        .catch(err => {
            dispatch(returnErrors(err.response, 'GET_EXCHANGE_RATES_FAIL'))
            dispatch({
                type: GET_EXCHANGE_RATES_FAIL,
            })
        })
}

export const getBalance = () => dispatch => {
  dispatch({
    type: GET_BALANCE
  })

  axiosInstance.get('accounts/balance/')
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
