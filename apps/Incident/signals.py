from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import EmergencyIncident


@receiver(post_save, sender=EmergencyIncident)
def broadcast_incident(sender, instance, created, **kwargs):
    if not created:
        return

    channel_layer = get_channel_layer()

    data = {
        "id": instance.id,
        "type": instance.incident_type,
        "description": instance.description,
        "latitude": instance.latitude,
        "longitude": instance.longitude,
        "status": instance.status,
        "created_at": str(instance.created_at),
    }

    print(data)

    async_to_sync(channel_layer.group_send)(
        "emergency_incidents",
        {
            "type": "emergency_alert",
            "data": data
        }
    )