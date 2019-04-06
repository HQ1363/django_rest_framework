# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import re
import uuid
from datetime import datetime, timedelta

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password

from .models import *

re_tel = r'1[36789]\d{9}'


class TelcodeSerializers(serializers.ModelSerializer):
    tel = serializers.CharField(max_length=11, min_length=11)

    class Meta:
        model = Telcode
        fields = ('tel',)

    def validate(self, attrs):
        if not re.match(re_tel, attrs['tel']):
            raise ValidationError('手机格式不对')
        m1_ago = datetime.now() - timedelta(minutes=1)
        if Telcode.objects.filter(tel=attrs['tel'], addtime__gt=m1_ago):
            raise ValidationError('一分钟只能发一次')
        return attrs


class RegisterSerializers(serializers.ModelSerializer):
    pwd2 = serializers.CharField(max_length=16, min_length=6)
    code = serializers.CharField(max_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'pwd2', 'tel', 'code')

    def validate(self, attrs):
        if attrs['password'] != attrs['pwd2']:
            raise ValidationError('两次密码不一致')
        m5_ago = datetime.now() - timedelta(minutes=5)
        if Telcode.objects.filter(tel=attrs['tel'], addtime__lt=m5_ago).count():
            raise ValidationError('验证码过期')
        if not Telcode.objects.filter(tel=attrs['tel'], code=attrs['code']).count():
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
        user = User.objects.filter(Q(tel=attrs['username']) | Q(username=attrs['username'])).first()
        if user:
            if check_password(attrs['password'], user.password):
                key = uuid.uuid4()
                Token.objects.update_or_create(defaults={'key': key}, user=user)
                attrs['key'] = key
                return attrs
        raise ValidationError('用户名或密码错误')


class GoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    user_order = OrderSerializers(many=True)

    class Meta:
        model = User
        fields = '__all__'


class GoodstypeSerializers(serializers.ModelSerializer):
    goods_type = GoodsSerializers(many=True)
    goods_order = OrderSerializers(many=True)

    class Meta:
        model = GoodsType
        fields = '__all__'
