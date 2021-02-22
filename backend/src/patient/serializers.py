from rest_framework import serializers
from .models import Patient

# Convert model instance to JSON so frontend can recieve data

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'