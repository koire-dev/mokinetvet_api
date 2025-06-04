from django.db import models

from consultations.models import Consultation
from mokinetvet_api import settings


class UserMessage(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, null=True, blank=True, related_name='userMessages')
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

