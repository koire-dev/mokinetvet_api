from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import AnimalHealthRecord
from .serializers import AnimalHealthRecordSerializer

class AnimalHealthRecordViewSet(viewsets.ModelViewSet):
    queryset = AnimalHealthRecord.objects.all()
    serializer_class = AnimalHealthRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'eleveur':
            return AnimalHealthRecord.objects.filter(user=user)
        return AnimalHealthRecord.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'eleveur':
            raise PermissionDenied("Seuls les éleveurs peuvent enregistrer des dossiers de santé.")
        serializer.save(user=user)

    def perform_update(self, serializer):
        record = self.get_object()
        if record.user != self.request.user:
            raise PermissionDenied("Vous ne pouvez modifier que vos propres dossiers de santé.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("Vous ne pouvez supprimer que vos propres dossiers de santé.")
        instance.delete()
