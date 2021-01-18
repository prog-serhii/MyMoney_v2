from django.urls import path

from .views import WalletListAPI, WalletDetailAPI, WalletTotalBalanceAPI


urlpatterns = [
    path('wallets/', WalletListAPI.as_view(), name='api-wallet-list'),
    path('wallets/<int:pk>/', WalletDetailAPI.as_view(), name='api-wallet-detail'),
    path('wallets/balance/', WalletTotalBalanceAPI.as_view(), name='api-total-balance')
]
