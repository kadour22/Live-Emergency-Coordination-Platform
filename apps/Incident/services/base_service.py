from ..models import EmergencyIncident
from ..serializers import create_emergency_serializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
class EmergencyIncidentService :

    def create_report_emergency_incident(self,data,reporter) :
        serializer = create_emergency_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        report_data = serializer.save(reporter=reporter)

        return {
            "report_data":create_emergency_serializer(report_data).data
        }

    def report_emergency_incident_list(self) :
        return EmergencyIncident.objects.select_related(
            "reporter"
        ).all()
    
    def report_emergency_incident_by_id(self, incident_id):
        return get_object_or_404(
            EmergencyIncident, id = incident_id
        )
