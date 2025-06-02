from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from .models import Animal
from .serializers import AnimalSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Uniquement les animaux de l’éleveur connecté
        user = self.request.user
        if user.role == 'eleveur':
            return Animal.objects.filter(user=user)
        return Animal.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'eleveur':
            raise PermissionDenied("Seuls les éleveurs peuvent enregistrer des animaux.")
        serializer.save(user=user)

    def perform_update(self, serializer):
        animal = self.get_object()
        if animal.user != self.request.user:
            raise PermissionDenied("Vous ne pouvez modifier que vos propres animaux.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("Vous ne pouvez supprimer que vos propres animaux.")
        instance.delete()

    @action(detail=False, methods=['get'], url_path='mes-animaux')
    def mes_animaux(self, request):
        """Lister les animaux de l’éleveur connecté."""
        if request.user.role != 'eleveur':
            return Response({"detail": "Action réservée aux éleveurs."}, status=403)
        animaux = self.get_queryset()
        serializer = self.get_serializer(animaux, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='detail')
    def detail_animal(self, request, pk=None):
        """Obtenir le détail d’un animal spécifique (si propriétaire)."""
        try:
            animal = Animal.objects.get(pk=pk, user=request.user)
        except Animal.DoesNotExist:
            return Response({"detail": "Animal non trouvé ou non autorisé."}, status=404)
        serializer = self.get_serializer(animal)
        return Response(serializer.data)
