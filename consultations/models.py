from django.db import models
from django.conf import settings
from animals.models import Animal

class Consultation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('in_progress', 'En cours'),
        ('completed', 'Terminée'),
        ('cancelled', 'Annulée'),
    ]

    TYPE_CHOICES = [
        ('video', 'Vidéo'),
        ('audio', 'Audio'),
        ('chat', 'Chat'),
        ('terrain', 'Terrain'),
    ]

    animal = models.ForeignKey('animals.Animal', on_delete=models.CASCADE, related_name='consultations')
    vet = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                            related_name='consultations')
    symptoms = models.TextField()
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    consultation_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='chat')
    scheduled_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Consultation #{self.id} - {self.animal.name}"

