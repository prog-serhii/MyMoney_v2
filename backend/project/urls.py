from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, include


schema_view = get_schema_view(
    openapi.Info(
        title="MyMone API",
        default_version='v1',
        description="MyMoney API documentation",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kazmiruk.sergii@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('apps.user.urls')),
    path('api/', include('apps.wallet.urls')),
    path('api/', include('apps.action.urls'))
]
