import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { logout } from '../actions/auth'


const Navbar = ({ logout, isAuthenticated }) => {
    const guestLinks = () => (
        <Fragment>
            <Link className='nav-link' to='/login'>Login</Link>
            <Link className='nav-link' to='/signup'>Sing up</Link>
        </Fragment>
    );

    const authLinks = () => (
        <Fragment>
            <a className='nav-link' href='#' onClick={logout}>Logout</a>
        </Fragment>
    );

    return (
        <nav className='navbar navbar-expand-lg navbar-light bg-light'>
            <Link className='navbar-brand' to='/'>Auth System</Link>
            <button
                className='navbar-toggler'
                type='button'
                data-toggle='collapse'
                data-target='#navbarNavAltMarkup'
                aria-controls='navbarNavAltMarkup'
                aria-expanded='false'
                aria-label='Toggle navigation'
            >
                <span className='navbar-toggler-icon'></span>
            </button>
            <div className='collapse navbar-collapse' id='navbarNavAltMarkup'>
                <div className='navbar-nav'>
                    <Link className='nav-link active' to='/'>Home <span class='sr-only'>(current)</span></Link>
                    {isAuthenticated ? authLinks() : guestLinks()}
                </div>
            </div>
        </nav>
    );
};

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, { logout })(Navbar);