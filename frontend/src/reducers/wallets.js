import {
    GET_WALLETS_FAIL,
    GET_WALLETS_SUCCESS
} from '../actions/types'


const initialState = {
    wallets: [],
    isLoading: false
}

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_WALLETS_SUCCESS:
            return {
                ...state,
                wallets: action.payload,
                isLoading: false
            }
        case GET_WALLETS_FAIL:
            return {
                ...state,
                wallets: [],
                isLoading: false
            }
        default:
            return state
    }
}