# myapp/serializers.py
from rest_framework import serializers
from .models import GenericData

class GenericDataSerializer(serializers.ModelSerializer):
    data = serializers.JSONField()  # Override to allow any JSON structure

    class Meta:
        model = GenericData
        fields = ['id', 'data', 'created_at']
