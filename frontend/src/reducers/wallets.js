import {
    GET_WALLETS_FAIL,
    GET_WALLETS_SUCCESS,
    GET_WALLET_DETAIL_SUCCESS,
    GET_WALLET_DETAIL_FAIL
} from '../actions/types'


const initialState = {
    wallets: [],
    balance: {},
    walletDetail: {}
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

        case GET_WALLET_DETAIL_SUCCESS:
            return {
                ...state,
                walletDetail: action.payload
            }

        case GET_WALLET_DETAIL_FAIL:
            return {
                ...state,
                walletDetail: {}
            }

        default:
            return state
    }
}