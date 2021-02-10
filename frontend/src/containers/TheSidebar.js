import React, { Component } from 'react'
import { connect } from 'react-redux'
import {
  CCreateElement,
  CSidebar,
  CSidebarBrand,
  CSidebarNav,
  CSidebarNavDivider,
  CSidebarNavTitle,
  CSidebarMinimizer,
  CSidebarNavDropdown,
  CSidebarNavItem,
} from '@coreui/react'

import CIcon from '@coreui/icons-react'

// sidebar nav config
import navigation from './_nav'

import { toggleSidebar } from '../actions/template'


class TheSidebar extends Component {

  render() {
    return (
      <CSidebar
        show={this.props.sidebarShow}
        onShowChange={(val) => this.props.toggleSidebar(val)}
      >
        <CSidebarBrand className="d-md-down-none" to="/">
          <CIcon
            className="c-sidebar-brand-full"
            name="logo-negative"
            height={35}
          />
          <CIcon
            className="c-sidebar-brand-minimized"
            name="sygnet"
            height={35}
          />
        </CSidebarBrand>
        <CSidebarNav>

          <CCreateElement
            items={navigation}
            components={{
              CSidebarNavDivider,
              CSidebarNavDropdown,
              CSidebarNavItem,
              CSidebarNavTitle
            }}
          />
        </CSidebarNav>
        <CSidebarMinimizer className="c-d-md-down-none" />
      </CSidebar>
    )
  }
}

const mapStateToProps = state => ({
  sidebarShow: state.templateReducer.sidebarShow
})

export default connect(mapStateToProps, { toggleSidebar })(React.memo(TheSidebar))
