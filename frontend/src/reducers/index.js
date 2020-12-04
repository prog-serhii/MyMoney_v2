import { combineReducers } from 'redux';

import nav from './nav'
import auth from './auth'

export default combineReducers({
    nav,
    auth
})

