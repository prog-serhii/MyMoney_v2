from .views import SignUpView
from django.urls import path
from rest_framework_simplejwt.views import \
    TokenRefreshView, TokenObtainPairView


app_name = 'apps.user'

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('token/obtain/', TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
