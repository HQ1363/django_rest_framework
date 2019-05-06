# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from datetime import datetime, timedelta

from rest_framework.authentication import BaseAuthentication

from .models import Token


# 自定义token认证: 设置token，30分钟后失效
class MyToken(BaseAuthentication):
    def authenticate(self, request):
        """
        Authenticate the request and return a two-tuple of (user, token).
        """
        key = request.query_params.get('key')
        token = Token.objects.filter(key=key).first()
        if token:
            m30_ago = datetime.now() - timedelta(minutes=30)
            if token.updatetime < m30_ago:
                return None, None
            return token.user, token
        return None, None
