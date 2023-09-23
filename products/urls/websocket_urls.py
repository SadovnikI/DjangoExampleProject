from django.urls import path

from products.websockets import consumer

websocket_urlpatterns = [
    path("ws/admin-socket/messages", consumer.AdminMessagesConsumer.as_asgi()),
]
