from django.urls import re_path
from .consumers import EmergencyIncidentConsumer

websocket_urlpatterns = [
    re_path(r'^ws/incidents/$', EmergencyIncidentConsumer.as_asgi()),
]