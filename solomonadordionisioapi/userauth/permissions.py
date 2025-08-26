from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allow full access to admin users; read-only for everyone else.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff
