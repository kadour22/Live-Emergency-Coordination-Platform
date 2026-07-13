from ..models import EmergencyIncident
from ..serializers import create_emergency_serializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
class EmergencyIncidentService :

    def create_report_emergency_incident(self, data, reporter):
        serializer = create_emergency_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        incident = serializer.save(reporter=reporter)

        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            "emergency_incident",
            {
                "type": "emergency_alert",
                "data": create_emergency_serializer(incident).data,
            },
        )
        print("emergency alert sent to websocket")
        return {
            "report_data": create_emergency_serializer(incident).data
        }
    def report_emergency_incident_list(self) :
        return EmergencyIncident.objects.select_related(
            "reporter"
        ).all()
    
    def report_emergency_incident_by_id(self, incident_id):
        return get_object_or_404(
            EmergencyIncident, id = incident_id
        )
