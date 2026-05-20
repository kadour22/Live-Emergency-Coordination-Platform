import json
from channels.generic.websocket import AsyncWebsocketConsumer


class EmergencyIncidentConsumer(AsyncWebsocketConsumer) :

    async def connect(self) :

        self.groupe_name = "emergency_incident"
        await self.channel_layer.groupe_add(
            self.groupe_name,
            self.channel_name
        )

    async def disconnect(self, close_code ) :
        await self.channel_layer.groupe_discard(
            self.groupe_name,
            self.channel_name
        )

    async def send_emergency_incident(self, event):
        await self.send(text_data=json.dumps({
            "type": "send_emergency_incident",
            "data": event["data"],
        }))

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer
# from .models import EmergencyIncident


# @receiver(post_save, sender=EmergencyIncident)
# def broadcast_incident(sender, instance, created, **kwargs):
#     if not created:
#         return

#     channel_layer = get_channel_layer()

#     data = {
#         "id": instance.id,
#         "type": instance.incident_type,
#         "description": instance.description,
#         "latitude": instance.latitude,
#         "longitude": instance.longitude,
#         "status": instance.status,
#         "created_at": str(instance.created_at),
#     }

#     async_to_sync(channel_layer.group_send)(
#         "emergency_incidents",
#         {
#             "type": "emergency_alert",
#             "data": data
#         }
#     )