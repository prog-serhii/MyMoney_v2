from django.urls import path

from .views import WalletListView, WalletDetailView


urlpatterns = [
    path('wallets/', WalletListView.as_view(), name='api-wallet-list'),
    path('wallets/<uuid:pk>/', WalletDetailView.as_view(), name='api-wallet-detail'),
]
