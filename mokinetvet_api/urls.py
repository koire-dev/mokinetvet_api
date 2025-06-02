from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mokinetvet_api import settings

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
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
