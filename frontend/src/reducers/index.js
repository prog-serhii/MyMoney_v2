import { combineReducers } from 'redux'
import template from './template'
import auth from './auth'
import errors from './errors'
import wallets from './wallets'

export default combineReducers({
    templateReducer: template,
    authReducer: auth,
    errorsReducer: errors,
    walletsReducer: wallets
})