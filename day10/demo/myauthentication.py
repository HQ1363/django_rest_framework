# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework.authentication import BaseAuthentication

from .models import Token


class TokenAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token', '')
        if token:
            token_obj = Token.objects.filter(token=token).first()
            if token_obj:
                # token_obj.user_id赋值给request.user
                # token赋值给request.auth
                return token_obj.user, token
        # raise AuthenticationFailed('身份认证未通过')
        return None, None
