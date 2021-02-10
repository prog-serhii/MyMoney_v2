import { TOGGLE_SIDEBAR } from './types'


export const toggleSidebar = (val) => dispatch => {
    dispatch({
        type: TOGGLE_SIDEBAR,
        sidebarShow: val
    })
}