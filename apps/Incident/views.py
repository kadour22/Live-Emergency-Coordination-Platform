from rest_framework.views import APIView
from rest_framework.response import Response
from .services.base_service import EmergencyIncidentService
from .serializers import emergency_serializer, create_emergency_serializer

class EmergencyIncidentView(APIView) :

    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.incident_data_service = EmergencyIncidentService()


    def get(self, request, incident_id=None) :
        
        if incident_id is not None :
            incident = self.incident_data_service.report_emergency_incident_by_id(incident_id = incident_id)
            serializer = emergency_serializer(incident, many=False)
            return Response(serializer.data, status=201)
        
        incidents = self.incident_data_service.report_emergency_incident_list()
        serializer = emergency_serializer(incidents, many = True)
        return Response(serializer.data, status=201)