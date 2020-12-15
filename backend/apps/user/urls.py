from django.urls import path, include

from .views import UserProfileView, AllCurrencuesView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('user/', UserProfileView.as_view(), name='api-current-user'),
    path('currencies/', AllCurrencuesView.as_view(), name='api-all-available-currencies')
]
