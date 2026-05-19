from rest_framework import serializers
from .models import EmergencyIncident

class user_serializer(serializers.ModelSerializer) :
    class Meta :
        model  = User
        fields = ["username"]
class emergency_serializer(serializers.ModelSerializer) :
    created_by = user_serializer(read_only = True)
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