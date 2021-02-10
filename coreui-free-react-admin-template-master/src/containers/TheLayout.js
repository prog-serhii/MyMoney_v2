import React, { useEffect } from 'react'
import { connect } from 'react-redux'

import {
  TheContent,
  TheSidebar,
  TheFooter,
  TheHeader
} from './index'
import { checkAuthenticated } from '../actions/auth'


const TheLayout = (props) => {
  useEffect(() => {
    props.checkAuthenticated();
    //props.loadUser();
  }, [])

  return (
    <div className="c-app c-default-layout">
      <TheSidebar />
      <div className="c-wrapper">
        <TheHeader />
        <div className="c-body">
          <TheContent />
        </div>
        <TheFooter />
      </div>
    </div>
  )
}

export default connect(null, { checkAuthenticated })(TheLayout)
