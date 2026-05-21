from django.db import models
from django.contrib.auth.models import User

class EmergencyIncident(models.Model) :

    class IncidentChoices(models.TextChoices) :

        fire     = "fire", "Fire"
        flood    = "flood", "Flood"
        accident = "accident", "Accident"
        robbery  = "robbery", "Robbery"
        medical  = "medical", "Medical"
    
    reporter      = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "emergency_reports")
    incident_type = models.CharField(max_length=100, choices = IncidentChoices.choices)
    description   = models.TextField()
    latitude      = models.FloatField()
    longitude     = models.FloatField()
    status        = models.CharField(default="pending",max_length=20)
    created_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.incident_type

