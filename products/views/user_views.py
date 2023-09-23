from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.renderers import JSONRenderer

from products.models import CustomUser
from products.serializers.user_serializers import UserSerializer, CreateOrUpdateUserSerializer
from products.utils.permission import IsAuthenticatedOrPost


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing the accounts
    associated with the user.
    """

    renderer_classes = [JSONRenderer]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrPost]

    def get_queryset(self):
        """
        Superusers have access to all items and regular only to what they own
        """
        if self.request.user.is_superuser:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return CreateOrUpdateUserSerializer
        return UserSerializer
