from rest_framework import serializers
from .models import Diagnostic

class DiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostic
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
