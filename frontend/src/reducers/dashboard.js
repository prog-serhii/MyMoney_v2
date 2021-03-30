import {
    GET_EXCHANGE_RATES,
    GET_EXCHANGE_RATES_SUCCESS,
    GET_EXCHANGE_RATES_FAIL,
    GET_BALANCE,
    GET_BALANCE_SUCCESS,
    GET_BALANCE_FAIL
} from '../actions/types'

const initialState = {
    rates: [],
    baseCurrency: '',
    exchangeRatesLoading: false,
    
    balance: {},
    balanceLoading: false
}

export default function (state = initialState, action) {
    switch(action.type) {
        case GET_EXCHANGE_RATES:
            return {
                ...state,
                exchangeRatesLoading: true
            }

        case GET_EXCHANGE_RATES_SUCCESS:
            return {
                ...state,
                rates: action.payload.rates,
                baseCurrency: action.payload.baseCurrency,
                exchangeRatesLoading: false
            }

        case GET_EXCHANGE_RATES_FAIL:
            return {
                ...state,
                rates: [],
                baseCurrency: '',
                exchangeRatesLoading: false
            }
        
        case GET_BALANCE:
            return {
                ...state,
                balanceLoading: true
            }

        case GET_BALANCE_SUCCESS:
            return {
                ...state,
                balance: action.payload,
                balanceLoading: false
            }

        case GET_BALANCE_FAIL:
            return {
                ...state,
                balance: {},
                balanceLoading: false
            }
            
        default:
            return state
    }
}