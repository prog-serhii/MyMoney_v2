import React from 'react';

const SignUp = React.lazy(() => import('./App/containers/SignUp'));
const SignIn = React.lazy(() => import('./App/containers/SignIn'));
const PasswordReset = React.lazy(() => import('./App/containers/PasswordReset'));

const route = [
    { path: '/signup', exact: true, name: 'SignUp', component: SignUp },
    { path: '/login', exact: true, name: 'SignIn', component: SignIn },
    { path: '/password/reset', exact: true, name: 'PasswordReser', comment: PasswordReset }
];

export default route;