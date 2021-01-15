from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/', include('apps.user.urls')),
    path('api/', include('apps.wallet.urls')),
    path('api/', include('apps.action.urls'))
]
