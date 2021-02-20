from django.urls import path

from .views import AccountListAPI, AccountDetailAPI, AccountTotalBalanceAPI
# , AccountStatisticAPI


urlpatterns = [
    path('accounts/',
         AccountListAPI.as_view(), name='api-accounts-list'),
    path('accounts/<int:pk>/',
         AccountDetailAPI.as_view(), name='api-accounts-detail'),
    path('accounts/balance/',
         AccountTotalBalanceAPI.as_view(), name='api-accounts-total-balance'),
]
