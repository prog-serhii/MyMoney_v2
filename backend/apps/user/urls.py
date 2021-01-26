from django.urls import path, include

# from .views import UserProfileView, AllCurrencuesView, CurrenciesRates

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('user/', UserProfileView.as_view(), name='api-current-user'),
    # path('user/currencies/', CurrenciesRates.as_view()),
    # path('currencies/', AllCurrencuesView.as_view(), name='api-all-available-currencies'),
]
