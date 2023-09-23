from rest_framework.permissions import BasePermission


class IsAuthenticatedOrPost(BasePermission):
    """
    Allows access only to authenticated users except POST method.
    """

    SAFE_METHODS = ['POST']

    def has_permission(self, request, view):
        return bool(
            request.method in self.SAFE_METHODS
            or request.user and request.user.is_authenticated
        )
