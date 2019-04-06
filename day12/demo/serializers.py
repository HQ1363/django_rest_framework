# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import re
from datetime import datetime, timedelta

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

from .models import User, Code

re_tel = r'1[356789]\d{9}'


# 短信验证码序列化器
class CodeSerializers(serializers.ModelSerializer):
    # 可能需要重复修改添加验证码，将唯一性验证去掉，重写tel
    tel = serializers.CharField(max_length=11, min_length=11)

    class Meta:
        model = Code
        fields = ('tel',)

    def validate(self, attrs):
        if not re.match(re_tel, attrs['tel']):
            raise ValidationError('手机格式不正确')
        # 获取一分钟之前的时间
        m1_ago = datetime.now() - timedelta(minutes=1)
        # 验证用户获取验证码的时间有没有超过一分钟
        if Code.objects.filter(tel=attrs['tel'], addtime__gt=m1_ago).count():
            raise ValidationError('时间还没到1分钟，请稍后发送')
        return attrs


# 注册序列化
class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=16, min_length=6)
    # 添加数据库中没有的字段
    pwd2 = serializers.CharField(max_length=16, min_length=6, write_only=True)
    code = serializers.CharField(max_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'pwd2', 'tel', 'code')

    def validate(self, attrs):
        if attrs['password'] != attrs['pwd2']:
            raise ValidationError('两次密码不一致')
        # 验证用户验证码是不是已过期（5分钟）
        m5_ago = datetime.now() - timedelta(minutes=5)
        code = Code.objects.filter(tel=attrs['tel']).first()
        if code:
            if attrs['code'] != code.code:
                raise ValidationError('验证码错误')
            if code.addtime < m5_ago:
                raise ValidationError('验证码过期')
        # 去掉数据库中没有字段
        del attrs['pwd2']
        del attrs['code']
        # 用户密码加密
        attrs['password'] = make_password(attrs['password'])
        return attrs
