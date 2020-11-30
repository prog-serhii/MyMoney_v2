import React from 'react';
import { Link } from 'react-router-dom';


const Home = () => (
    <div className='container'>
        <div className='jumbotron mt-5'>
            <h1 className='display-4'>Welcome to Auth System!</h1>
            <p className='lead'>MyMoney_v2</p>
            <hr className='my-4' />
            <p>Click the Log In button!</p>
            <Link className='btn btn-primary btn-lg' to='/login' role='button'>Log In</Link>
        </div>
    </div>
);

export default Home;