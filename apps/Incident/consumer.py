import json
from channels.generic.websocket import AsyncWebsocketConsumer

class EmergencyIncidentConsumer(AsyncWebsocketConsumer) :

    async def connect(self) :

        self.group_name = "emergency_incident"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
        print("websocket connected")
    async def disconnect(self, close_code ) :
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        print("disconnected")
    async def emergency_alert(self, event):

        await self.send(text_data=json.dumps({
            "type": "emergency_alert",
            "data": event["data"],
        }))