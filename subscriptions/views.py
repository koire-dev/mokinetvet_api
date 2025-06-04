from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action
from .models import Subscription
from .serializers import SubscriptionSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'eleveur':
            return Subscription.objects.filter(user=user)
        if user.role == 'admin':
            return Subscription.objects.all()
        return Subscription.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'eleveur':
            raise PermissionDenied("Seuls les éleveurs peuvent souscrire à un abonnement.")
        serializer.save(user=user)

    def perform_update(self, serializer):
        subscription = self.get_object()
        if subscription.user != self.request.user and self.request.user.role != 'admin':
            raise PermissionDenied("Vous ne pouvez modifier que vos propres abonnements.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user and self.request.user.role != 'admin':
            raise PermissionDenied("Vous ne pouvez supprimer que vos propres abonnements.")
        instance.delete()

    @action(detail=False, methods=['get'], url_path='my-subscription')
    def my_subscription(self, request):
        """Retourne l’abonnement actif de l’utilisateur connecté"""
        abonnement = Subscription.objects.filter(user=request.user).order_by('-start_date').first()
        if not abonnement:
            return Response({"detail": "Aucun abonnement actif trouvé."}, status=404)
        serializer = self.get_serializer(abonnement)
        return Response(serializer.data)
