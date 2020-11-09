from django.urls import path

from .views import WalletListCreateView


urlpatterns = [
    path('wallets/', WalletListCreateView.as_view(), name='api-wallet-list'),
]
