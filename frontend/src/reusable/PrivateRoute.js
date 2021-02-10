import React, { Component } from 'react'
import { Route, Redirect } from 'react-router-dom'
import { connect } from 'react-redux'
import PropTypes from 'prop-types'

const PrivateRoute = ({ component: Component, auth, ...rest }) => (
    <Route
        {...rest}
        render={props => {
            return <Component {...props} />
        }}
    />
)

const mapStateToProps = state => ({
    auth: state.authReducer
})

export default connect(mapStateToProps)(PrivateRoute)