"""
ASGI config for DjangoExampleProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

import products.urls.websocket_urls

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoExampleProject.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    "websocket":
        AuthMiddlewareStack(
            URLRouter(products.urls.websocket_urls.websocket_urlpatterns)
        )
})
