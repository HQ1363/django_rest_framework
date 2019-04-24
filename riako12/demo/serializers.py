# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import re
import uuid
from datetime import datetime, timedelta

from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

from .models import Code, User, Token

re_tel = r'1[356789]\d{9}'


class CodeSerializers(serializers.ModelSerializer):
    tel = serializers.CharField(max_length=11, min_length=11)

    class Meta:
        model = Code
        fields = ('tel',)

    def validate(self, attrs):
        if re.match(attrs['tel'], re_tel):
            raise ValidationError('手机号格式不正确')
        m1_ago = datetime.now() - timedelta(minutes=1)
        if Code.objects.first(tel=attrs['tel'], addtime_gt=m1_ago):
            raise ValidationError('时间未到一分钟，无法发送')
        return attrs
