from django.urls import path

from .views import (AccountListAPI, AccountDetailAPI,
                    AccountTotalBalanceAPI, CurrenciesAPI, CurrencyRatesAPI)


urlpatterns = [
    path('accounts/',
         AccountListAPI.as_view(), name='api-accounts-list'),
    path('accounts/<int:pk>/',
         AccountDetailAPI.as_view(), name='api-accounts-detail'),
    path('accounts/balance/',
         AccountTotalBalanceAPI.as_view(), name='api-accounts-total-balance'),

    path('currencies/',
         CurrenciesAPI.as_view(), name='api-currencies'),
    path('currencies/rates/',
         CurrencyRatesAPI.as_view(), name='api-currency-rates')
]
