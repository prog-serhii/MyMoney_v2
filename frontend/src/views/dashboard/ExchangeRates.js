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
import CIcon from '@coreui/icons-react'

import { getExchangeRates } from '../../actions/dashboard'

const ExchangeRates = (props) => {

    useEffect(() => {
      props.getExchangeRates()
    }, [])

    const listRates = props.rates.map((rate) =>
      <CListGroupItem key={rate.code}>
        {`1 ${props.currency} = ${rate.rate} ${rate.code}`}
      </CListGroupItem>
    )

    return (
      <>
        <CCard color="gradient-secondary">
          <CCardHeader>
            Card with icon
            <div className="card-header-actions">
              <CIcon name="cil-check" className="float-right"/>
            </div>
          </CCardHeader>
            <CCardBody>
              {props.loading
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

export default connect(mapStateToProps, mapDispatchToProps)(ExchangeRates)