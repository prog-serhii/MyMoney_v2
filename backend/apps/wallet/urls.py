from django.urls import path

from .views import WalletListView, CreateWalletView, WalletDetailView


urlpatterns = [
    path('wallets/', WalletListView.as_view(), name='api-wallet-list'),
    path('wallets/add/', CreateWalletView.as_view(), name='api-create-wallet'),
    path('wallets/<uuid:pk>/', WalletDetailView.as_view(), name='api-wallet-detail'),
]
