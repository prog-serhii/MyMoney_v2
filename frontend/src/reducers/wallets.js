import {
    GET_WALLETS_FAIL,
    GET_WALLETS_SUCCESS,
    GET_BALANCE_SUCCESS,
    GET_BALANCE_FAIL
} from '../actions/types'


const initialState = {
    wallets: [],
    balance: {},
}

export default function (state = initialState, action) {
    switch (action.type) {

        case GET_WALLETS_SUCCESS:
            return {
                ...state,
                wallets: action.payload,
            }

        case GET_WALLETS_FAIL:
            return {
                ...state,
                wallets: [],
            }

        case GET_BALANCE_SUCCESS:
            return {
                ...state,
                balance: action.payload
            }

        case GET_BALANCE_FAIL:
            return {
                ...state,
                balance: {}
            }

        default:
            return state
    }
}