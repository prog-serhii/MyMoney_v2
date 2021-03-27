from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/rosetta/', include('rosetta.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('apps.common.urls'))
]
