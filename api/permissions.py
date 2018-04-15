from oauth2_provider.contrib.rest_framework import permissions


class PublicEndpoint(permissions.BasePermission):
    def has_permission(self, request, view):
        return True
