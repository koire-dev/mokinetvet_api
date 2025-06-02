from django.urls import path

from diseaseGuides.views import DiseaseGuideViewSet

urlpatterns = [
    path('disease-guides/', DiseaseGuideViewSet.as_view({'get': 'list'}), name='diseaseguide-list'),
    path('disease-guides/<int:pk>/', DiseaseGuideViewSet.as_view({'get': 'retrieve'}), name='diseaseguide-detail'),
]
