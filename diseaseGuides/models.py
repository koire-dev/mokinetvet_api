from django.db import models

class DiseaseGuide(models.Model):
    disease_name = models.CharField(max_length=100)
    description = models.TextField()
    symptoms = models.TextField()
    treatments = models.TextField()
    language = models.CharField(max_length=20, default='fr')
    access_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

