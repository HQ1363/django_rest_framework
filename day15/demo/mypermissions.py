# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework.permissions import BasePermission
from rest_framework import permissions


# 自定义权限：用户只能操作自己
class MyPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


# 自定义权限：只有某类用户可访问
class UserPermissions(BasePermission):
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.user.is_staff == '3'
