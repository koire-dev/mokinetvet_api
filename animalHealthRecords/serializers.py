from rest_framework import serializers
from .models import AnimalHealthRecord

class AnimalHealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalHealthRecord
        fields = '__all__'
        read_only_fields = ['id']
