from django.db import models

from consultations.models import Consultation


class Diagnostic(models.Model):
    SOURCE_CHOICES = [
        ('AI', 'IA'),
        ('vet', 'Vétérinaire'),
    ]

    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='diagnostics')
    diagnosis = models.TextField()
    validated_by_vet = models.BooleanField(default=False)
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
