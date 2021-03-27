from django.urls import path, include


urlpatterns = [
    path('', include('apps.authentication.urls')),
    path('', include('apps.account.urls')),
    path('', include('apps.transaction.urls'))
]
