import { GET_ERRORS, CLEAR_ERRORS } from './types'


export const returnErrors = (response, id) => {
  let payload = {
    msg: [],
    status: null,
    id: 'NO_RESPONSE'
  }

  // if a server response exist
  if (response) {
    payload = {
      msg: response.data.errors[0].message,
      status: response.status,
      id
    }
  }

  return {
    type: GET_ERRORS,
    payload
  }

}

export const clearErrors = () => {
  return {
    type: CLEAR_ERRORS
  }
}
