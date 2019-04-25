# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import re
from datetime import datetime, timedelta

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Code

tel_re = r'1[356789]\d{9}'


class CodeSerializers(serializers.ModelSerializer):
    tel = serializers.CharField(max_length=11, min_length=11)

    class Meta:
        model = Code
        fields = ('tel',)

    def validate(self, attrs):
        if not re.match(tel_re, attrs['tel']):
            raise ValidationError('手机号格式不正确')
        m1_ago = datetime.now() - timedelta(minutes=1)
        if Code.objects.first(tel=attrs['tel'], addtime_gt=m1_ago).count():
            raise ValidationError('一分钟只能发送一条验证码')
        return attrs
