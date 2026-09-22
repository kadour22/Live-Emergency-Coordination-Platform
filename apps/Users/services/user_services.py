from django.contrib.auth.models import User
from apps.Users.serializers import user_serializer, ChangePasswordSerializer
from apps.Incident.models import EmergencyIncident
from django.shortcuts import get_object_or_404

class UserService :

    def create_new_user(self, data) :

        serializer = user_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.save()
        return {
            "new_user_data": user_serializer(user_data).data
        }
    
    def change_user_password(self, data, user):
        serializer = ChangePasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user.set_password(serializer.validated_data["new_password"])
        user.save()

        return {
            "message": "Password updated successfully"
        }

class IncidentService:

    def get_all_incidents(self,user):
        incidents = EmergencyIncident.objects.filter(reporter=user)
        return incidents

    def get_incident_by_id(self, incident_id):
        incident = get_object_or_404(EmergencyIncident, id=incident_id)
        return incident
    
