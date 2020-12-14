import React, { useState } from 'react';
import { Redirect } from 'react-router-dom';
import { connect } from 'react-redux';

import '../../assets/scss/style.scss';
import Aux from '../../hoc/_Aux';
import Breadcrumb from '../layout/AdminLayout/Breadcrumb';
import { reset_password } from '../../actions/auth';


const PasswordReset = ({ reset_password }) => {
    const [requestSent, setRequestSent] = useState(false);

    const [email, setEmail] = useState('');

    const onChange = e => setEmail(e.target.value)

    const onSubmit = e => {
        e.preventDefault();

        reset_password(email);
        setRequestSent(true);
    };

    if (requestSent) {
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
                            <h3 className='mb-4'>Request Password: Reset</h3>
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
                                <button className='btn btn-primary shadow-2 mb-4' type='submit'>Reset Password</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </Aux >
    );
};


export default connect(null, { reset_password })(PasswordReset);