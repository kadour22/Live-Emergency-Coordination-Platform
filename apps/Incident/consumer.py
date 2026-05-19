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
    
    # def send_emergency_incident(self,event) :
    #     await self.send(text_data=json.dumps({
    #         "send_emergency_incident",
    #         "data": event["data"],
    #     }))
    async def send_emergency_incident(self, event):
        await self.send(text_data=json.dumps({
            "type": "send_emergency_incident",
            "data": event["data"],
        }))