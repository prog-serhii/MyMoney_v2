import React from 'react';

const SignUp = React.lazy(() => import('./App/containers/SignUp'));
const SignIn = React.lazy(() => import('./App/containers/SignIn'));
const PasswordReset = React.lazy(() => import('./App/containers/PasswordReset'));
const PasswordResetConfirm = React.lazy(() => import('./App/containers/PasswordResetConfirm'));

const route = [
    { path: '/signup', exact: true, name: 'SignUp', component: SignUp },
    { path: '/login', exact: true, name: 'SignIn', component: SignIn },
    { path: '/password/reset', exact: true, name: 'PasswordReset', component: PasswordReset },
    {
        path: '/password/reset/confirm/:uid/:token', exact: true,
        name: 'PasswordResetConfirm', component: PasswordResetConfirm
    }
];

export default route;