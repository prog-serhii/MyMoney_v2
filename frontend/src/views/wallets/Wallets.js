import React, { useEffect, useState } from 'react'
import { connect } from 'react-redux'

import {
  CCard,
  CCardBody,
  CCardHeader,
  CCol,
  CDataTable,
  CRow,
  CButton,
  CCollapse,
  CCallout
} from '@coreui/react'
import CIcon from '@coreui/icons-react'

import { getWallets, getBalance } from '../../actions/wallets'
import RemoveWalletModal from './RemoveWalletModal'

const formatCurrency = (amount, currency) => {
  return Intl.NumberFormat('de-DE', {
    currency: currency,
    style: 'currency',
    currencyDisplay: 'symbol'
  }).format(amount)
}


const getIcon = status => {
  switch (status) {
    case 'card':
      return (
        <CIcon name="cib-cc-visa" size={'lg'} />
      )
    case 'cashe':
      return (
        <CIcon name="cil-euro" size={'lg'} />
      )
    default:
      return status
  }
}


const Wallets = (props) => {
  const [editPanel, setEditPanel] = useState(null)

  useEffect(() => {
    props.getWallets()
    props.getBalance()
  }, [])

  const toggleEditPanel = (index) => {
    if (editPanel === index) {
      setEditPanel(null)
    } else {
      setEditPanel(index)
    }
  }

  const fields = [
    {
      filter: false,
      label: 'Type',
      key: 'wallet_type',
      _style: { width: '1%' },
    },
    'name',
    {
      filter: false,
      key: 'balance'
    },
    {
      key: 'show_details',
      label: '',
      _style: { width: '1%' },
      filter: false,
    }
  ]

  return (
    <>
      <CRow>
        <CCol>
          <CCard>
            <CCardHeader>
              Bordered Table
            </CCardHeader>
            <CCardBody>
              <CRow>
                <CCol>
                  <CCallout color="warning">
                    <small className="text-muted">Total balance:</small>
                    <br />
                    <strong className="h4">
                      {props.balance.amount &&
                        formatCurrency(props.balance.amount, props.balance.currency)
                      }
                    </strong>
                  </CCallout>
                </CCol>
              </CRow>
              <CRow>
                <CDataTable
                  hover
                  items={props.wallets}
                  fields={fields}
                  columnFilter
                  scopedSlots={{
                    'wallet_type':
                      (item) => (
                        <td>
                          <div className="text-center">{getIcon(item.wallet_type)}</div>
                        </td>
                      ),
                    'balance':
                      (item) => (
                        <td>
                          {formatCurrency(item.balance, item.currency)}
                        </td>
                      ),
                    'show_details':
                      (item) => {
                        const editButton = (
                          <CButton
                            variant="ghost"
                            color="info"
                            size="sm"
                            onClick={() => { toggleEditPanel(item.pk) }}
                          >
                            <CIcon name="cil-pencil" />
                          </CButton>
                        )

                        const closeButton = (
                          <CButton
                            variant="ghost"
                            color="danger"
                            size="sm"
                            onClick={() => { toggleEditPanel(item.pk) }}
                          >
                            <CIcon name="cil-x-circle" />
                          </CButton>
                        )

                        return (
                          <td className="py-2">
                            {editPanel !== item.pk
                              ? editButton
                              : closeButton
                            }
                          </td>
                        )
                      },
                    'details':
                      (item) => {
                        return (
                          <CCollapse show={editPanel === item.pk}>
                            <CCardBody>
                              <CButton color="success" className="btn-square">
                                Save
                            </CButton>
                              <CButton
                                color="danger"
                                className="btn-square ml-1"
                                onClick={() => setConfirmModal(!confirmModal)}
                              >
                                Delete
                            </CButton>
                            </CCardBody>
                          </CCollapse>
                        )
                      }
                  }}
                />
              </CRow>
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>
      <RemoveWalletModal id={null} />
    </>
  )
}

const mapStateToProps = state => {
  return {
    wallets: state.walletsReducer.wallets,
    balance: state.walletsReducer.balance,
    errors: state.errorsReducer
  }
}

const mapDispatchToProps = dispatch => {
  return {
    getWallets: () => dispatch(getWallets()),
    getBalance: () => dispatch(getBalance())
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Wallets)
