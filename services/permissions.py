from rest_framework import permissions


class IsServiceProviderOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return ((request.user.is_authenticated) and (request.user.role == 'is_provider')) or (request.user.is_staff)
    
class IsServiceProvider(permissions.BasePermission):
    def has_permission(self, request, view):
        return ((request.user.is_authenticated) and (request.user.role == 'is_provider'))


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (obj.user == request.user) and (request.user.is_authenticated)
