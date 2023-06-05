from rest_framework import permissions


class IsServiceProviderOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return ((request.user.is_authenticated) and (request.user.role == 'is_provider')) or (request.user.is_staff)
    
class IsCustomerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return ((request.user.is_authenticated) and (request.user.role == 'is_customer')) or (request.user.is_staff)
    
class IsCustomerAndIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return ((request.user.is_authenticated) and (request.user.role == 'is_customer'))
    

class IsServiceOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (obj.provider.user == request.user) or (request.user.is_staff)
    
class IsAppointmentOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (obj.provider.user == request.user) or (request.user.is_staff)

