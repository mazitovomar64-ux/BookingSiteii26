from rest_framework import permissions
from .models import *


class CheckRole(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'client'


class CheckOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'owner'
