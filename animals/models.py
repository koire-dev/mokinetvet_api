from django.db import models
from django.conf import settings

class Animal(models.Model):
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='animals')
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField()
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    name = models.CharField(max_length=50)
    identification_tag = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.species})"
