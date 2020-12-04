import React, { useState } from 'react';
import { NavLink, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';

import '../../assets/scss/style.scss';
import Aux from '../../hoc/_Aux';
import Breadcrumb from '../layout/AdminLayout/Breadcrumb';
import { login } from '../../actions/auth';


const SignIn = ({ login, isAuthenticated }) => {
    const [formData, setFormData] = useState({
        email: '',
        password: ''
    });

    const { email, password } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = e => {
        e.preventDefault();

        login(email, password);
    };

    if (isAuthenticated) {
        return <Redirect to='/' />
    }

    return (
        <Aux>
            <Breadcrumb />
            <div className='auth-wrapper'>
                <div className='auth-content'>
                    <div className='auth-bg'>
                        <span className='r' />
                        <span className='r s' />
                        <span className='r s' />
                        <span className='r' />
                    </div>
                    <div className='card'>
                        <div className='card-body text-center'>
                            <div className='mb-4'>
                                <i className='feather icon-unlock auth-icon' />
                            </div>
                            <h3 className='mb-4'>Login</h3>
                            <form onSubmit={e => onSubmit(e)}>
                                <div className='input-group mb-3'>
                                    <input
                                        type='email'
                                        className='form-control'
                                        placeholder='Email'
                                        name='email'
                                        value={email}
                                        onChange={e => onChange(e)}
                                        required
                                    />
                                </div>
                                <div className='input-group mb-4'>
                                    <input
                                        type='password'
                                        className='form-control'
                                        placeholder='password'
                                        name='password'
                                        value={password}
                                        onChange={e => onChange(e)}
                                        minLength='6'
                                        required
                                    />
                                </div>
                                <div className='form-group text-left'>
                                    <div className='checkbox checkbox-fill d-inline'>
                                        <input type='checkbox' name='checkbox-fill-1' id='checkbox-fill-a1' />
                                        <label htmlFor='checkbox-fill-a1' className='cr'> Save credentials</label>
                                    </div>
                                </div>
                                <button className='btn btn-primary shadow-2 mb-4' type='submit'>Login</button>
                            </form>
                            <p className='mb-2 text-muted'>Forgot password? <NavLink to='/password/resset'>Reset</NavLink></p>
                            <p className='mb-0 text-muted'>Don’t have an account? <NavLink to='/signup'>Signup</NavLink></p>
                        </div>
                    </div>
                </div>
            </div>
        </Aux>
    );
};

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});


export default connect(mapStateToProps, { login })(SignIn);