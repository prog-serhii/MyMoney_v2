from django.urls import path

from .views import (AccountListAPI, AccountDetailAPI, AccountTotalBalanceAPI,
                    AvailableCurrenciesAPI, UsersCurrenciesAPI)


urlpatterns = [
    path('accounts/',
         AccountListAPI.as_view(), name='api-accounts-list'),
    path('accounts/<int:pk>/',
         AccountDetailAPI.as_view(), name='api-accounts-detail'),
    path('accounts/balance/',
         AccountTotalBalanceAPI.as_view(), name='api-accounts-total-balance'),

    path('available_currencies/',
         AvailableCurrenciesAPI.as_view(), name='api-available-currencies'),
    path('users_currencies/',
         UsersCurrenciesAPI.as_view(), name='api-users-currencies'),
    #     path('users_rates/',
    #          UsersRatesAPI.as_view(), name='api-users-rates')
]
