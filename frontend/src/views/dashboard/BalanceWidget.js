import React, { useEffect } from 'react'
import { connect } from 'react-redux'
import {
  CWidgetIcon,
  CCardFooter,
  CLink,
  CSpinner
} from  '@coreui/react'
import { freeSet } from '@coreui/icons'
import CIcon from '@coreui/icons-react'

import { getBalance } from '../../actions/dashboard'


const BalanceWidget = (props) => {
  const { loading, balance } = props
  const { getBalance } = props

  useEffect(() => {
    getBalance()
  }, [])

  let formatedBalance = <CSpinner className="text-center" />

  if (loading == false && balance.amount) {
    formatedBalance = `${balance.amount} ${balance.currency}`
  }

  return (
    <CWidgetIcon 
      text="balance" 
      header={formatedBalance} 
      color="warning" 
      iconPadding={false}
      footerSlot={
        <CCardFooter className="card-footer px-3 py-2">
          <CLink
            className="font-weight-bold font-xs btn-block text-muted"
            to="/register"
          >
            View more
            <CIcon name="cil-arrow-right" className="float-right" width="16"/>
          </CLink>
        </CCardFooter>
      }
    >
      <CIcon width={24} content={freeSet.cilCash}/>
    </CWidgetIcon>
  )
}

const mapStateToProps = state => {
  return {
    loading: state.dashboardReducer.balanceLoading,
    balance: state.dashboardReducer.balance,
    errors: state.errorsReducer
  }
}

const mapDispatchToProps = dispatch => {
  return {
    getBalance: () => dispatch(getBalance())
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(BalanceWidget)