# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework.throttling import SimpleRateThrottle, AnonRateThrottle


# 未认证用户限流
class NoAuth(SimpleRateThrottle):
    # 指定限流速率字段
    scope = 'nauth'

    def get_cache_key(self, request, view):
        # 根据认证方法，来判断用户是否认证通过
        if request.user:
            return None
        return self.cache_format % {
            'scope': self.scope,
            # 获取用户ip识别用户
            'ident': self.get_ident(request)
        }


# 通过认证用户限流
class YesAuth(SimpleRateThrottle):
    scope = 'yauth'

    def get_cache_key(self, request, view):
        if request.user:
            ident = request.user.id
        else:
            ident = self.get_ident(request)
        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }
