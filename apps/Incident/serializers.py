from rest_framework import serializers
from .models import EmergencyIncident

class emergency_serializer(serializers.ModelSerializer) :

    class Meta :
        model  = EmergencyIncident
        fields = [
            "id",
            "reporter",
            "incident_type",
            "description",
            "latitude",
            "longitude",
            "status",
            "created_at"
        ]

class create_emergency_serializer(serializers.ModelSerializer) :

    class Meta :
        model  = EmergencyIncident
        fields = [
            "reporter",
            "incident_type",
            "description",
            "latitude",
            "longitude",
            "status",
        ]
        read_only_fields = ["reporter"]