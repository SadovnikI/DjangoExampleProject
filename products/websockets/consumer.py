from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from products.utils.constants import ADMIN_GROUP_NAME


class AdminMessagesConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = ADMIN_GROUP_NAME

        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.channel_name
        )
        if self.scope["user"].is_authificated and self.scope["user"].is_superuser:
            self.accept()
