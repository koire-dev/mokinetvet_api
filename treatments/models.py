from django.db import models

from consultations.models import Consultation


class Treatment(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='treatments')
    treatment = models.TextField()
    recommended_drugs = models.TextField()
    follow_up_days = models.IntegerField()

