from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from .models import Diagnostic
from .serializers import DiagnosticSerializer

class DiagnosticViewSet(viewsets.ModelViewSet):
    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'eleveur':
            return Diagnostic.objects.filter(user=user)
        return Diagnostic.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'veterinaire':
            raise PermissionDenied("Seuls les veterinaires peuvent créer des diagnostics.")
        serializer.save()

    def perform_update(self, serializer):
        diagnostic = self.get_object()
        if diagnostic.user != self.request.user:
            raise PermissionDenied("Vous ne pouvez modifier que vos propres diagnostics.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("Vous ne pouvez supprimer que vos propres diagnostics.")
        instance.delete()

    @action(detail=False, methods=['get'], url_path='mes-diagnostics')
    def mes_diagnostics(self, request):
        """Lister les diagnostics de l’éleveur connecté."""
        if request.user.role != 'eleveur':
            return Response({"detail": "Action réservée aux éleveurs."}, status=403)
        diagnostics = self.get_queryset()
        serializer = self.get_serializer(diagnostics, many=True)
        return Response(serializer.data)
