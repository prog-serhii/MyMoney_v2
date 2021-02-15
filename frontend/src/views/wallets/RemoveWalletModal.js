import React, { useState } from 'react'
import { connect } from 'react-redux'

import {
  CModal,
  CModalBody,
  CModalFooter,
  CModalHeader,
  CModalTitle,
} from '@coreui/react'

import { removeWallet } from '../../actions/wallets'


const RemoveWalletModal = (props) => {
  const [confirmModal, setConfirmModal] = useState(false)

  const handleRemoveWallet = (id) => {
    props.removeWallet(id)
  }

  return (
    <CModal
      color="danger"
      show={confirmModal}
      onClose={setConfirmModal}
    >
      <CModalHeader closeButton>
        <CModalTitle>Modal title</CModalTitle>
      </CModalHeader>
      <CModalBody>
        Ви підтверджуєте видалення даного гаманця?
      </CModalBody>
      <CModalFooter>
        <CButton
          color="danger"
          onClick={handleRemoveWallet(props.id)}
        >
          Delete
          </CButton>
        <CButton
          className="ml-2"
          color="secondary"
          onClick={() => setConfirmModal(false)}
        >Cancel</CButton>
      </CModalFooter>
    </CModal>
  )
}


const mapDispatchToProps = dispatch => {
  return {
    removeWallet: () => dispatch(removeWallet())
  }
}

export default connect(null, mapDispatchToProps)(RemoveWalletModal)