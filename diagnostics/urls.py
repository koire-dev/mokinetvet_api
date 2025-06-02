from django.urls import path
from diagnostics.views import DiagnosticViewSet

urlpatterns = [
    path('diagnostics/create/', DiagnosticViewSet.as_view({'post': 'create'}), name='diagnostic-create'),
    path('diagnostics/mine/', DiagnosticViewSet.as_view({'get': 'mes_diagnostics'}), name='diagnostic-mine'),
    path('diagnostics/<int:pk>/', DiagnosticViewSet.as_view({'get': 'retrieve'}), name='diagnostic-detail'),
    path('diagnostics/<int:pk>/update/', DiagnosticViewSet.as_view({'put': 'update'}), name='diagnostic-update'),
    path('diagnostics/<int:pk>/partial-update/', DiagnosticViewSet.as_view({'patch': 'partial_update'}), name='diagnostic-partial-update'),
    path('diagnostics/<int:pk>/delete/', DiagnosticViewSet.as_view({'delete': 'destroy'}), name='diagnostic-delete'),
]
