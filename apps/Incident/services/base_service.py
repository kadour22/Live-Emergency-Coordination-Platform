from ..models import EmergencyIncident
from ..serializers import create_emergency_serializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .helper import send_emergency_alert

class EmergencyIncidentService :

    def incident_list(self):
        return EmergencyIncident.objects.select_related("reporter").all()
    
    def create_incident(self, data, reporter):
        serializer = create_emergency_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        incident = serializer.save(reporter=reporter)
        send_emergency_alert(incident)
        return {
            "report_data": create_emergency_serializer(incident).data
        }

    def get_incident(self, incident_id):
        return get_object_or_404(
            EmergencyIncident, id = incident_id
        )
