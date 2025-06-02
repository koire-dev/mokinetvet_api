from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action
from .models import Consultation
from .serializers import ConsultationSerializer

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'eleveur':
            return Consultation.objects.filter(animal__user=user)
        elif user.role == 'veterinaire':
            return Consultation.objects.filter(vet=user)
        elif user.role == 'admin':
            return Consultation.objects.all()
        return Consultation.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'eleveur':
            raise PermissionDenied("Seuls les éleveurs peuvent créer une consultation.")
        serializer.save()

    @action(detail=False, methods=['get'], url_path='mes-consultations')
    def mes_consultations(self, request):
        consultations = self.get_queryset()
        serializer = self.get_serializer(consultations, many=True)
        return Response(serializer.data)
