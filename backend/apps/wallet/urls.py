from django.urls import path

from .views import WalletListAPI, WalletDetailAPI, WalletTotalBalanceAPI
# , WalletStatisticAPI


urlpatterns = [
    path('wallets/', WalletListAPI.as_view(), name='api-wallets-list'),
    path('wallets/<int:pk>/', WalletDetailAPI.as_view(), name='api-wallets-detail'),
    path('wallets/balance/', WalletTotalBalanceAPI.as_view(), name='api-wallets-total-balance'),
    # path('wallets/<int:pk>/statistic/', WalletStatisticAPI.as_view(), name='api-wallet-statistic')
]
