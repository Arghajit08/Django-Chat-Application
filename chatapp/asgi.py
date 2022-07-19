"""
ASGI config for chatapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')

application = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chats.consumers import ChatConsumer

ws_pattern = [
    path('chat/<room_code>', ChatConsumer.as_asgi()),

]

application = ProtocolTypeRouter({
    'websocket':(URLRouter(ws_pattern)) 
})
