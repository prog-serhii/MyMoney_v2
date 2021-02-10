import { Link, Redirect } from 'react-router-dom'
import React from 'react'
import {
  CButton,
  CCard,
  CCardBody,
  CCardFooter,
  CCol,
  CContainer,
  CForm,
  CInput,
  CSpinner,
  CInputGroup,
  CInputGroupPrepend,
  CInputGroupText,
  CInvalidFeedback,
  CRow
} from '@coreui/react'
import CIcon from '@coreui/icons-react'
import { connect } from 'react-redux'
import { login } from '../../../actions/auth'
import { clearErrors } from '../../../actions/errors'

class Login extends React.Component {
  state = {
    email: '',
    password: '',
    errors: {}
  }

  componentDidUpdate(prevProps) {
    const { errors } = this.props
    if (errors !== prevProps.errors) {
      // Check for login errors
      if (errors.id === 'LOGIN_FAIL') {
        this.setState({ errors: errors.msg })
      } else {
        this.setState({ errors: {} })
      }
    }
  }

  onSubmit = e => {
    e.preventDefault()

    // Remove all errors from global state
    this.props.clearErrors()

    this.props.login(this.state.email, this.state.password)
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value })
  }

  render() {
    const { email, password } = this.state;

    if (this.props.isAuthenticated) {
      return <Redirect to='/' />
    }

    return (
      <div className="c-app c-default-layout flex-row align-items-center">
        <CContainer>
          <CRow className="justify-content-center">
            <CCol md="9" lg="7" xl="6">
              <CCard className="mx-4">
                <CCardBody className="p-4">
                  <CForm onSubmit={this.onSubmit}>
                    <h1>Login</h1>
                    <p className="text-muted">Sinin in your account.</p>
                    <CInputGroup className="mb-3">
                      <CInputGroupPrepend>
                        <CInputGroupText>@</CInputGroupText>
                      </CInputGroupPrepend>
                      <CInput
                        name="email"
                        value={email}
                        onChange={this.onChange}
                        type="text"
                        placeholder="Email"
                        autoComplete="email"
                      />
                    </CInputGroup>
                    <CInputGroup className="mb-3">
                      <CInputGroupPrepend>
                        <CInputGroupText>
                          <CIcon name="cil-lock-locked" />
                        </CInputGroupText>
                      </CInputGroupPrepend>
                      <CInput
                        name="password"
                        value={password}
                        onChange={this.onChange}
                        type="password"
                        placeholder="Password"
                        autoComplete="password"
                      />
                    </CInputGroup>
                    <CButton
                      type="submit"
                      color="success"
                      block
                    >
                      Login
                    </CButton>
                  </CForm>
                </CCardBody>
                <CCardFooter className="p-4">
                  <CRow>
                    <CCol>
                      <p className="text-center mb-1">Does'n have an acount?</p>
                    </CCol>
                  </CRow>
                  <CRow>
                    <CCol>
                      <div className="text-center">
                        <Link to="/register" className="text-decoration-none">
                          <CButton variant="ghost" color="success">
                            <CIcon name="cil-user-follow" /> Register
                        </CButton>
                        </Link>
                      </div>
                    </CCol>
                  </CRow>
                </CCardFooter>
              </CCard>
            </CCol>
          </CRow>
        </CContainer>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  isAuthenticated: state.authReducer.isAuthenticated,
  errors: state.errorsReducer
})

export default connect(mapStateToProps, { login, clearErrors })(Login)
