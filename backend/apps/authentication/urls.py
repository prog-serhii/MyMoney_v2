from django.urls import path, include

from rest_framework_simplejwt import views


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/jwt/create/',
         views.TokenObtainPairView.as_view(), name='api-jwt-create'),
    path('auth/jwt/refresh/',
         views.TokenRefreshView.as_view(), name='api-jwt-refresh'),
    path('auth/jwt/verify/',
         views.TokenVerifyView.as_view(), name='api-jwt-verify')
]
