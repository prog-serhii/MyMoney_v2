import { combineReducers } from 'redux'
import template from './template'
import auth from './auth'
import errors from './errors'


export default combineReducers({
    templateReducer: template,
    authReducer: auth,
    errorsReducer: errors
})