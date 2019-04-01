# -*- coding: utf-8 -*-
# -*- author: GXR -*-
import uuid
import re
from datetime import datetime, timedelta

from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.exceptions import ValidationError

from .models import *

tel_re = r'1[35789]\d{9}'


# 短信验证码序列化器
class CodeSerializers(serializers.ModelSerializer):
    # 可能需要重复修改添加验证码，将唯一性验证去掉，重写tel
    tel = serializers.CharField(max_length=11)

    class Meta:
        model = Code
        fields = '__all__'

    def validate(self, attrs):
        if not re.match(tel_re, attrs['tel']):
            raise ValidationError('手机格式不正确')
        # 获取之前的时间
        one_minutes_ago = datetime.now() - timedelta(minutes=5)
        # 验证用户获取验证码的时间有没有超过一分钟
        if Code.objects.filter(tel=attrs['tel'], add_time__gt=one_minutes_ago).count():
            raise ValidationError('时间还没到1分钟，请稍后发送')
        return attrs


class RegisterSerializers(serializers.ModelSerializer):
    pwd2 = serializers.CharField(max_length=64, min_length=6, write_only=True)

    class Meta:
        model = User
        fieldds = '__all__'

    def validate(self, attrs):
        # 效验两次密码是否相等
        if attrs['pwd2'] != attrs['password']:
            raise ValidationError('两次输入密码不符')
        # 验证用户验证码是不是已过期（5分钟）
        code_obj = Code.objects.filter(tel=attrs['tel']).first()
        five_minutes_ago = datetime.now() - timedelta(minutes=5)
        if code_obj:
            if attrs['code'] != code_obj.code:
                raise ValidationError('验证码错误')
            if code_obj.add_time < five_minutes_ago:
                raise ValidationError('验证码过期')
        # 去掉数据库中没有字段
        del attrs['pwd2']
        del attrs['code']
        # 用户密码加密
        attrs['password'] = make_password(attrs['password'])
        return attrs

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class LoginSerializers(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length=16, min_length=6)

    class Meta:
        model = User
        fieldds = '__all__'

    def validate(self, attrs):
        # 效验密码用户名是否通过验证
        user = User.objects.filter(username=attrs['user_name']).first()
        if user:
            if check_password(attrs['password'], user.password):
                key = uuid.uuid4()
                Token.objects.update_or_create(defaults={'key': key}, user=user)
                return attrs
        raise ValidationError('用户名或密码错误')


class GoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fieldds = '__all__'


class TpyeSerializers(serializers.ModelSerializer):
    goods = GoodsSerializers(many=True)

    class Meta:
        model = Type
        fieldds = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fieldds = '__all__'
