import imp
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from notifier.consumers import NotificationConsumer

application = ProtocolTypeRouter(
    {
        "websocket": AuthMiddlewareStack(
            URLRouter(
                [
                    path("notifications/", NotificationConsumer().as_asgi()),
                ]
            )
        )
    }
)
