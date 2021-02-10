import { TOGGLE_SIDEBAR } from '../actions/types';


const initialState = {
    sidebarShow: 'responsive'
}

export default function (state = initialState, action) {
    switch (action.type) {
        case TOGGLE_SIDEBAR:
            return {
                ...state,
                sidebarShow: action.sidebarShow
            }
        default:
            return state
    }
}