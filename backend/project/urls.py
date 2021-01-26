from django.contrib import admin
from django.urls import path, include

apipatterns = [
    path('', include('apps.user.urls')),
    path('', include('apps.wallet.urls')),
    path('', include('apps.action.urls'))
]

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/', include(apipatterns))
]
