from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_emergency_alert(incident):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "emergency_incident",
        {
            "type": "emergency_alert",
            "data": incident,
        },
    )