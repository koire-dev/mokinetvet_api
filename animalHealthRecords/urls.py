from django.urls import path

from animalHealthRecords.views import AnimalHealthRecordViewSet

urlpatterns = [
    path('health-records/create/', AnimalHealthRecordViewSet.as_view({'post': 'create'}), name='healthrecord-create'),
    path('health-records/', AnimalHealthRecordViewSet.as_view({'get': 'list'}), name='healthrecord-list'),
    path('health-records/<int:pk>/', AnimalHealthRecordViewSet.as_view({'get': 'retrieve'}), name='healthrecord-detail'),
    path('health-records/<int:pk>/update/', AnimalHealthRecordViewSet.as_view({'put': 'update'}), name='healthrecord-update'),
    path('health-records/<int:pk>/partial-update/', AnimalHealthRecordViewSet.as_view({'patch': 'partial_update'}), name='healthrecord-partial-update'),
    path('health-records/<int:pk>/delete/', AnimalHealthRecordViewSet.as_view({'delete': 'destroy'}), name='healthrecord-delete'),
]
