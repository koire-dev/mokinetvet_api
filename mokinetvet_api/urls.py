from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from mokinetvet_api import settings

schema_view = get_schema_view(
    openapi.Info(
        title="MOKINEVET API",
        default_version='v1',
        description="Documentation de l'API MOKINEVET",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@mokinevet.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
print(">>> URLs chargés pour la prod <<<")

urlpatterns = [
    path('api/', include('users.urls')),
    path('api/', include('animals.urls')),
    path('api/', include('consultations.urls')),
    path('api/', include('diagnostics.urls')),
    path('api/', include('treatments.urls')),
    path('api/', include('userMessages.urls')),
    path('api/', include('notifications.urls')),
    path('api/', include('diseaseGuides.urls')),
    path('api/', include('subscriptions.urls')),
    path('api/', include('animalHealthRecords.urls')),

# Swagger & Redoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
