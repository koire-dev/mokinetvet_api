from rest_framework import serializers
from .models import DiseaseGuide

class DiseaseGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseGuide
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
