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
import { connect } from 'react-redux';
import { register } from '../../../actions/auth'
import { clearErrors } from '../../../actions/errors'

class Register extends React.Component {
  state = {
    name: '',
    email: '',
    password: '',
    re_password: '',
    errors: {}
  }

  componentDidUpdate(prevProps) {
    const { errors } = this.props
    if (errors !== prevProps.errors) {
      // Check for register errors
      if (errors.id === 'REGISTER_FAIL') {
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

    // Create a user object
    const newUser = {
      name: this.state.name,
      email: this.state.email,
      password: this.state.password,
      re_password: this.state.re_password
    }

    this.props.register(newUser)
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value })
  }

  render() {
    if (this.props.isRegistered) {
      return <Redirect to='/success' />
    }

    const { name, email, password, re_password, errors } = this.state;
    return (
      <div className="c-app c-default-layout flex-row align-items-center">
        <CContainer>
          <CRow className="justify-content-center">
            <CCol md="9" lg="7" xl="6">
              <CCard className="mx-4">
                <CCardBody className="p-4">
                  <CForm onSubmit={this.onSubmit}>
                    <h1>Register</h1>
                    <p className="text-muted">Create your account</p>
                    <CInputGroup className="mb-3">
                      <CInputGroupPrepend>
                        <CInputGroupText>
                          <CIcon name="cil-user" />
                        </CInputGroupText>
                      </CInputGroupPrepend>
                      <CInput
                        invalid={errors.name}
                        name="name"
                        value={name}
                        onChange={this.onChange}
                        type="text"
                        placeholder="Username"
                        autoComplete="name"
                      />
                      {
                        errors.name
                        &&
                        <CInvalidFeedback>{errors.name}</CInvalidFeedback>
                      }
                    </CInputGroup>
                    <CInputGroup className="mb-3">
                      <CInputGroupPrepend>
                        <CInputGroupText>@</CInputGroupText>
                      </CInputGroupPrepend>
                      <CInput
                        invalid={errors.email}
                        name="email"
                        value={email}
                        onChange={this.onChange}
                        type="text"
                        placeholder="Email"
                        autoComplete="email"
                      />
                      {
                        errors.email
                        && <CInvalidFeedback>{errors.email}</CInvalidFeedback>
                      }
                    </CInputGroup>
                    <CInputGroup className="mb-3">
                      <CInputGroupPrepend>
                        <CInputGroupText>
                          <CIcon name="cil-lock-locked" />
                        </CInputGroupText>
                      </CInputGroupPrepend>
                      <CInput
                        invalid={errors.password}
                        name="password"
                        value={password}
                        onChange={this.onChange}
                        type="password"
                        placeholder="Password"
                        autoComplete="new-password"
                      />
                      {
                        errors.password
                        && <CInvalidFeedback>{errors.password}</CInvalidFeedback>
                      }
                    </CInputGroup>
                    <CInputGroup className="mb-4">
                      <CInputGroupPrepend>
                        <CInputGroupText>
                          <CIcon name="cil-lock-locked" />
                        </CInputGroupText>
                      </CInputGroupPrepend>
                      <CInput
                        invalid={errors.re_password || errors.non_field_errors}
                        name="re_password"
                        value={re_password}
                        onChange={this.onChange}
                        type="password"
                        placeholder="Repeat password"
                        autoComplete="new-password"
                      />
                      {
                        errors.re_password
                        && <CInvalidFeedback>{errors.re_password}</CInvalidFeedback>
                      }
                      {
                        errors.non_field_errors
                        && <CInvalidFeedback>{errors.non_field_errors}</CInvalidFeedback>
                      }
                    </CInputGroup>
                    <CButton
                      // disabled={isLoading}
                      type="submit"
                      color="success"
                      block
                    >
                      {/* {
                        isLoading
                          ? <CSpinner className="mr-1" color="light" size="sm" />
                          : <>Create Account</>
                      } */}
                      Create Account
                    </CButton>
                  </CForm>
                </CCardBody>
                <CCardFooter className="p-4">
                  <CRow>
                    <CCol>
                      <p className="text-center mb-1">Already have an acount?</p>
                    </CCol>
                  </CRow>
                  <CRow>
                    <CCol>
                      <div className="text-center">
                        <Link to="/login" className="text-decoration-none">
                          <CButton variant="ghost" color="success">
                            <CIcon name="cil-chevron-right" /> Login
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
  isRegistered: state.authReducer.isRegistered,
  errors: state.errorsReducer
})

export default connect(mapStateToProps, { register, clearErrors })(Register)
