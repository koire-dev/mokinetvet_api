from django.urls import path
from .views import ConsultationViewSet

urlpatterns = [
    path('consultations/', ConsultationViewSet.as_view({'get': 'list', 'post': 'create'}), name='consultation-list-create'),
    path('consultations/mine/', ConsultationViewSet.as_view({'get': 'mes_consultations'}), name='consultation-mine'),
    path('consultations/<int:pk>/', ConsultationViewSet.as_view({'get': 'retrieve'}), name='consultation-detail'),
    path('consultations/<int:pk>/update/', ConsultationViewSet.as_view({'put': 'update'}), name='consultation-update'),
    path('consultations/<int:pk>/delete/', ConsultationViewSet.as_view({'delete': 'destroy'}), name='consultation-delete'),
]
