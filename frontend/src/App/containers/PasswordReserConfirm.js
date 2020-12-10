import React, { useState } from 'react';
import { Redirect } from 'react-router-dom';
import { connect } from 'react-redux';

import '../../assets/scss/style.scss';
import Aux from '../../hoc/_Aux';
import Breadcrumb from '../layout/AdminLayout/Breadcrumb';
import { reset_password_confirm } from '../../actions/auth';


const PasswordResetConfirm = ({ match, reset_password_confirm }) => {
    const [requestSent, setRequestSent] = useState(false);

    const [formData, setFormData] = useState({
        new_password: '',
        re_new_password: ''
    });

    const { new_password, re_new_password } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });


    const onSubmit = e => {
        e.preventDefault();

        const uid = match.params.uid;
        const token = match.params.token;

        reset_password_confirm(uid, token, new_password, re_new_password);
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
                                <div className='input-group mb-4'>
                                    <input
                                        type='password'
                                        className='form-control'
                                        placeholder='New Password'
                                        name='new_password'
                                        value={new_password}
                                        onChange={e => onChange(e)}
                                        minLength='6'
                                        required
                                    />
                                </div>
                                <div className='input-group mb-4'>
                                    <input
                                        type='password'
                                        className='form-control'
                                        placeholder='Confirm New Password'
                                        name='re_new_password'
                                        value={re_new_password}
                                        onChange={e => onChange(e)}
                                        minLength='6'
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


export default connect(null, { reset_password_confirm })(PasswordResetConfirm);