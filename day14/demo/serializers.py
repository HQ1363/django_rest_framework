# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import re
import uuid
from datetime import datetime, timedelta

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q

from .models import User, Token, Code, Guoji

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
        if Code.objects.filter(tel=attrs['tel'], addtime__gt=m1_ago).count():
            raise ValidationError('未到一分钟')
        return attrs


class RegisterSerializers(serializers.ModelSerializer):
    pwd2 = serializers.CharField(max_length=16, min_length=6)
    code = serializers.CharField(max_length=6)

    class Meta:
        model = User
        fields = ('username', 'password', 'pwd2', 'tel', 'code')

    def validate(self, attrs):
        if attrs['password'] != attrs['pwd2']:
            raise ValidationError('两次密码不一致')
        m5_ago = datetime.now() - timedelta(minutes=5)
        if Code.objects.filter(tel=attrs['tel'], addtime__lt=m5_ago).count():
            raise ValidationError('验证码过期')
        if not Code.objects.filter(tel=attrs['tel'], code=attrs['code']).count():
            raise ValidationError('验证码错误')
        del attrs['pwd2']
        del attrs['code']
        attrs['password'] = make_password(attrs['password'])
        return attrs


class LoginSerializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=16, min_length=6)
    key = serializers.CharField(max_length=128, required=False, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'key')

    def validate(self, attrs):
        user = User.objects.filter(Q(username=attrs['username']) | Q(tel=attrs['username'])).first()
        if user:
            if check_password(attrs['password'], user.password):
                key = uuid.uuid4()
                Token.objects.update_or_create(defaults={'key': key}, user=user)
                attrs['key'] = key
                return attrs
        raise ValidationError('用户名或密码错误')


class GuojiSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Guoji
        fields = '__all__'
