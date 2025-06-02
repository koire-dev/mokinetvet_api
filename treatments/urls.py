from django.urls import path
from treatments.views import TreatmentViewSet

urlpatterns = [
    path('treatments/create/', TreatmentViewSet.as_view({'post': 'create'}), name='treatment-create'),
    path('treatments/', TreatmentViewSet.as_view({'get': 'list'}), name='treatment-list'),
    path('treatments/<int:pk>/', TreatmentViewSet.as_view({'get': 'retrieve'}), name='treatment-detail'),
    path('treatments/<int:pk>/update/', TreatmentViewSet.as_view({'put': 'update'}), name='treatment-update'),
    path('treatments/<int:pk>/partial-update/', TreatmentViewSet.as_view({'patch': 'partial_update'}), name='treatment-partial-update'),
    path('treatments/<int:pk>/delete/', TreatmentViewSet.as_view({'delete': 'destroy'}), name='treatment-delete'),
]
