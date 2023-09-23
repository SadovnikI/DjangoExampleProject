from datetime import datetime
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer

from products.models.product_models import Product
from products.serializers.product_serializers import ProductSerializer, CreateOrUpdateProductSerializer
from products.utils.constants import ADMIN_GROUP_NAME, PRODUCT_URL, USER_URL
from products.websockets.utils import send_message_to_group


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing the Products.
    """
    renderer_classes = [JSONRenderer]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return CreateOrUpdateProductSerializer
        return ProductSerializer

    def get_queryset(self):
        """
        Superusers have access to all items and regular only to what they own
        """
        if self.request.user.is_superuser:
            return Product.objects.all()
        else:
            return Product.objects.filter(user_owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save()
        # sending message to admin user websocket group
        send_message_to_group(
            ADMIN_GROUP_NAME,
            {
                "type": f"{ADMIN_GROUP_NAME}.send_message",
                "message": f"Product: {PRODUCT_URL.format(serializer.instance.uuid)} was added by "
                           f"{USER_URL.format(serializer.instance.user_owner.uuid)} "
                           f"Time: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
            })

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
