import React from 'react';
import { Provider } from 'react-redux';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Home from './containers/Home';
import Login from './containers/Login';
import Signup from './containers/Signup';
import Activate from './containers/Activate';
import ResetPassword from './containers/ResetPassword';
import ResetPasswordConfirm from './containers/ResetPasswordConfirm';
import Layout from './hocs/Layout';

import store from './store'


const App = () => (
    <Provider store={store}>
        <Router>
            <Layout>
                <Switch>
                    <Route exact path='/'><Home /></Route>
                    <Route path='/login'><Login /></Route>
                    <Route path='/signup'><Signup /></Route>
                    <Route path='/password/reset'><ResetPassword /></Route>
                    <Route path='/password/reset/confirm/:uid/:token'><ResetPasswordConfirm /></Route>
                    <Route path='/activate/:uid/:token'><Activate /></Route>
                </Switch>
            </Layout>
        </Router>
    </Provider>
);

export default App;