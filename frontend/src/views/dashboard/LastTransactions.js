import React, { useState, useEffect } from 'react'
import { connect } from 'react-redux'
import {
  CNav,
  CNavItem,
  CNavLink,
  CTabContent,
  CTabPane,
  CCard,
  CCardBody,
  CTabs,
  CCardHeader,
  CListGroup,
  CListGroupItem,
  CDataTable
} from '@coreui/react'
import { freeSet } from '@coreui/icons'
import CIcon from '@coreui/icons-react'

import { getIncomes, getExpenses } from '../../actions/dashboard'


const LastTransactions = (props) => {
  const [active, setActive] = useState(0)

  useEffect(() => {
    props.getIncomes(5)
    props.getExpenses(5)
  }, [])

  const incomeFields = [
    {
      key: 'name',
      label: 'Income'
    },
    {
      key: 'formatted_amount',
      label: 'Amount'
    },
    {
      key: 'date',
      label: 'Date'
    }
  ]

  const expenseFields = [
    {
      key: 'name',
      label: 'Expense'
    },
    {
      key: 'formatted_amount',
      label: 'Amount'
    },
    {
      key: 'date',
      label: 'Date'
    }
  ]


  return (
      <CCard>
        
        <CCardHeader>
          Last Transactions
        </CCardHeader>
        
        <CCardBody>
          <CTabs activeTab={active} onActiveTabChange={idx => setActive(idx)}>
            
            <CNav variant="tabs">
              <CNavItem>
                <CNavLink className="text-success">
                    <CIcon content={freeSet.cilArrowThickBottom}/>
                    { active === 0 && ' Incomes'}
                  </CNavLink>
                </CNavItem>
                <CNavItem>
                  <CNavLink className="text-danger">
                    <CIcon content={freeSet.cilArrowThickTop}/>
                    { active === 1 && ' Expenses'}
                  </CNavLink>
                </CNavItem>
              </CNav>
            
            <CTabContent>
              <CTabPane>
                <CDataTable
                  items={props.incomes}
                  fields={incomeFields}
                  clickableRows
                  onRowClick={(row) => console.log(row)}
                />
              </CTabPane>
              <CTabPane>
                <CDataTable
                  items={props.expenses}
                  fields={expenseFields}
                  hover
                  onRowClick={(row) => console.log(row)}
                />
              </CTabPane>
            </CTabContent>
          
          </CTabs>
        
        </CCardBody>
      
      </CCard>
    )
}


const mapStateToProps = state => {
    return {
        incomes: state.dashboardReducer.incomes.results,
        expenses: state.dashboardReducer.expenses.results,
        incomesLoading: state.dashboardReducer.incomesLoading,
        expensesLoading: state.dashboardReducer.expensesLoading,
        errors: state.errorsReducer
    }
}

const mapDispatchToProps = dispatch => {
  return {
    getIncomes: (limit) => dispatch(getIncomes(limit)),
    getExpenses: (limit) => dispatch(getExpenses(limit))
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(LastTransactions)