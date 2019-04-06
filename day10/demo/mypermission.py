# -*- coding: utf-8 -*-
# -*- author: GXR -*-

# IsAuthenticated 只有通过认证的用户才有权限
# AllowAny 允许所有用户
# IsAuthenticatedOrReadOnly 没认证的用户只能读取，认证过的用户才有增删改权限
# IsAdminUser 只有管理员才具有权限
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser


class MyPermissions(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.auth)

    def has_object_permission(self, request, view, obj):
        # 判断是不是增删改操作，是的话再判断当前评论是否属于该用户
        if request.method in ['PUT', 'DELETE', 'PATCH', 'POST']:
            if obj.user.id == request.user:
                return True
            else:
                return False
        return True
