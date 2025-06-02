from django.db import models

class AnimalHealthRecord(models.Model):
    animal = models.ForeignKey('animals.Animal', on_delete=models.CASCADE, related_name='health_records')
    description = models.TextField()
    date_of_record = models.DateField()

