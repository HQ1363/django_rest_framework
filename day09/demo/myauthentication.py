# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .models import Token


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token', '')
        if token:
            token_obj = Token.objects.filter(token=token).first()
            if token_obj:
                return token_obj.user, None
        raise AuthenticationFailed('验证失败')
