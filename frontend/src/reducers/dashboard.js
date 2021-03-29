import {
    GET_EXCHANGE_RATES,
    GET_EXCHANGE_RATES_SUCCESS,
    GET_EXCHANGE_RATES_FAIL
} from '../actions/types'

const initialState = {
    rates: [],
    baseCurrency: null,
    exchangeRatesLoading: false
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
                baseCurrency: null,
                exchangeRatesLoading: false
            }

        default:
            return state
    }
}