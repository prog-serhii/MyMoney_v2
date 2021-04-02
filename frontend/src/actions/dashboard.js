import axiosInstance from '../axios'
import {
  GET_EXCHANGE_RATES,
  GET_EXCHANGE_RATES_SUCCESS,
  GET_EXCHANGE_RATES_FAIL,
  GET_BALANCE,
  GET_BALANCE_SUCCESS,
  GET_BALANCE_FAIL,  
  GET_INCOMES,
  GET_INCOMES_SUCCESS,
  GET_INCOMES_FAIL,
  GET_EXPENSES,
  GET_EXPENSES_SUCCESS,
  GET_EXPENSES_FAIL
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

export const getIncomes = (limit) => dispatch => {
  dispatch({
    type: GET_INCOMES
  })

  let url = 'incomes/'
  if (limit) {
    url += `?limit=${limit}`
  }
  console.log(url)
  axiosInstance.get(url)
    .then(res => {
      dispatch({
        type: GET_INCOMES_SUCCESS,
        payload: res.data
      })
    })
    .catch(err => {
      dispatch(returnErrors(err.response, 'GET_INCOMES_FAIL'))
      dispatch({
        type: GET_INCOMES_FAIL
      })
    })
}

export const getExpenses = (limit) => dispatch => {
  dispatch({
    type: GET_EXPENSES
  })

  let url = 'expenses/'
  if (limit) {
    url += `?limit=${limit}`
  }

  axiosInstance.get(url)
    .then(res => {
      dispatch({
        type: GET_EXPENSES_SUCCESS,
        payload: res.data
      })
    })
    .catch(err => {
      dispatch(returnErrors(err.response, 'GET_EXPENSES_FAIL'))
      dispatch({
        type: GET_EXPENSES_FAIL
      })
    })
}