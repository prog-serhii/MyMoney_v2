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
  CCollapse
} from '@coreui/react'
import CIcon from '@coreui/icons-react'

import { getWallets } from '../../actions/wallets'


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
  const [editPanel, setEditPanel] = useState([])

  useEffect(() => {
    props.getWallets();
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
      _style: { width: '10%' },
      filter: false,
    }
  ]

  return (
    <CRow>
      <CCol>
        <CCard>
          <CCardHeader>
            Bordered Table
            </CCardHeader>
          <CCardBody>
            <CDataTable
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
                    return (
                      <td className="py-2">
                        <CButton
                          variant="ghost"
                          color="info"
                          size="sm"
                          onClick={() => { toggleEditPanel(item.pk) }}
                        >
                          <span><CIcon name="cil-pencil" /> Edit</span>
                        </CButton>
                      </td>
                    )
                  },
                'details':
                  (item) => {
                    return (
                      <CCollapse show={editPanel === item.pk}>
                        <CCardBody>
                          {item.name}
                        </CCardBody>
                      </CCollapse>
                    )
                  }
              }}
            />
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  )
}

const mapStateToProps = state => {
  return {
    wallets: state.walletsReducer.wallets,
    errors: state.errorsReducer
  }
}

const mapDispatchToProps = dispatch => {
  return {
    getWallets: () => dispatch(getWallets())
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Wallets)
