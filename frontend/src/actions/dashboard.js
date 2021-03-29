import axiosInstance from '../axios'
import {
    GET_EXCHANGE_RATES,
    GET_EXCHANGE_RATES_SUCCESS,
    GET_EXCHANGE_RATES_FAIL
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


