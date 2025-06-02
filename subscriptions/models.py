from django.db import models

from mokinetvet_api import settings


class Subscription(models.Model):
    TYPE_CHOICES = [
        ('free', 'Gratuit'),
        ('premium', 'Premium'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='free')
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

