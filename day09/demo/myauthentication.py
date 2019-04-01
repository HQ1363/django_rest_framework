# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Token


class MyAuth(BaseException):
    def authentication(self, request):
        key = request.query_params.get('key', '')
        if key:
            token = Token.objects.filter(key=key).first()
            if token:
                return (token.user, key)
        raise AuthenticationFailed('身份认证未通过')
