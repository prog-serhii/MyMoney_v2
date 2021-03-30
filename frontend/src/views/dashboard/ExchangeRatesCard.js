import React, { useEffect } from 'react'
import { connect } from 'react-redux'
import {
  CCard,
  CCardBody,
  CCardHeader,
  CListGroup,
  CListGroupItem,
  CSpinner,
} from  '@coreui/react'
import { freeSet } from '@coreui/icons'
import CIcon from '@coreui/icons-react'

import { getExchangeRates } from '../../actions/dashboard'

const ExchangeRatesCard = (props) => {
  const { loading, rates } = props
  const { getExchangeRates } = props

    useEffect(() => {
      getExchangeRates()
    }, [])

    const listRates = rates.map((rate) =>
      <CListGroupItem key={rate.code}>
        {`1 ${rate.code} = ${rate.rate} ${props.currency}`}
      </CListGroupItem>
    )

    return (
      <>
        <CCard color="gradient-secondary">
          <CCardHeader>
            Exchange Rates
            <div className="card-header-actions">
              <CIcon content={freeSet.cilBank} className="float-right"/>
            </div>
          </CCardHeader>
            <CCardBody>
              {loading
                ? <div className="text-center">
                    <CSpinner grow className="m-2" />
                    <CSpinner grow className="m-2" />
                    <CSpinner grow className="m-2" />
                  </div>
                : <CListGroup className="text-center">
                    {listRates}
                  </CListGroup>
              }
          </CCardBody>
        </CCard>
      </>
  )
}

const mapStateToProps = state => {
    return {
        loading: state.dashboardReducer.exchangeRatesLoading,
        rates: state.dashboardReducer.rates,
        currency: state.dashboardReducer.baseCurrency,
        errors: state.errorsReducer
    }
}

const mapDispatchToProps = dispatch => {
  return {
    getExchangeRates: () => dispatch(getExchangeRates())
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(ExchangeRatesCard)