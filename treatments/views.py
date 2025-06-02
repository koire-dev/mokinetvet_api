from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Treatment
from .serializers import TreatmentSerializer

class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'eleveur':
            return Treatment.objects.filter(user=user)
        return Treatment.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'eleveur':
            raise PermissionDenied("Seuls les éleveurs peuvent enregistrer des traitements.")
        serializer.save()

    def perform_update(self, serializer):
        treatment = self.get_object()
        if treatment.user != self.request.user:
            raise PermissionDenied("Vous ne pouvez modifier que vos propres traitements.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("Vous ne pouvez supprimer que vos propres traitements.")
        instance.delete()
