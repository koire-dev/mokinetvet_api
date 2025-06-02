from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from .models import UserMessage
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = UserMessage.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserMessage.objects.filter(recipient=user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def perform_update(self, serializer):
        message = self.get_object()
        if message.sender != self.request.user:
            raise PermissionDenied("Vous ne pouvez modifier que vos propres userMessages.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.sender != self.request.user:
            raise PermissionDenied("Vous ne pouvez supprimer que vos propres userMessages.")
        instance.delete()
