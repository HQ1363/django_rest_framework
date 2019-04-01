# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.auth)

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'DELETE', 'PATCH', 'POST']:
            if request.user == obj.user:
                return True
            else:
                return False
        return True
