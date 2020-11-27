import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Home from './containers/Home';
import Login from './containers/Login';
import Signup from './containers/Signup';
import Activate from './containers/Activate';
import ResetPassword from './containers/ResetPassword';
import ResetPasswordConfirm from './containers/ResetPasswordConfirm';
import Layout from './hocs/Layout';


const App = () => (
    <Router>
        <Layout>
            <Switch>
                <Router exact path='/'><Home /></Router>
                <Router exact path='/login'><Login /></Router>
                <Router exact path='/signup'><Signup /></Router>
                <Router exact path='/password/reset'><ResetPassword /></Router>
                <Router exact path='/password/reset/confirm/:uid/:token'><ResetPasswordConfirm /></Router>
                <Router exact path='/activate/:uid/:token'><Activate /></Router>
            </Switch>
        </Layout>
    </Router>
);

export default App;