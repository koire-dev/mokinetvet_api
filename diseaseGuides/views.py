from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import DiseaseGuide
from .serializers import DiseaseGuideSerializer

class DiseaseGuideViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DiseaseGuide.objects.all()
    serializer_class = DiseaseGuideSerializer
    permission_classes = [IsAuthenticated]
