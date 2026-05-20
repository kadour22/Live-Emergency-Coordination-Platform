from django.urls import path
from . import views
urlpatterns = [
    path("incidents_list/", views.EmergencyIncidentView.as_view()),
    path("incident/<int:incident_id>/details/", views.EmergencyIncidentView.as_view()),
]