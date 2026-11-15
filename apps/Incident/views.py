from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .services.base_service import EmergencyIncidentService
from .serializers import emergency_serializer, create_emergency_serializer

class EmergencyIncidentView(APIView) :
   
    permission_classes = [IsAdminUser]
  
    @property
    def service(self) :
        return EmergencyIncidentService()

    def get(self, request, incident_id=None) :
        
        if incident_id is not None :
            incident   = self.service.get_incident(incident_id = incident_id)
            serializer = emergency_serializer(incident, many=False)
            return Response(serializer.data, status=201)
        
        incidents  = self.service.incident_list()
        serializer = emergency_serializer(incidents, many = True)
        return Response(serializer.data, status=201)

class CreateEmergencyIncidentView(APIView) :
  
    permission_classes = [IsAuthenticated]
    @property
    def service(self) :
        return EmergencyIncidentService()

    
    def post(self, request) :    
        try:
            report_data = self.service.create_incident(
            data = request.data,
            reporter = request.user
        )
        
            return Response(report_data)
        except Exception as error:
            return Response({"error": str(error)}, status=400)
        