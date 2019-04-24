# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import uuid

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

from .models import User, Token


class SignupSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=16, min_length=6)
    pwd2 = serializers.CharField(max_length=16, min_length=6)

    class Meta:
        model = User
        fields = ('username', 'password', 'pwd2', 'age', 'tel')

    def validate(self, attrs):
        if attrs['password'] != attrs['pwd2']:
            raise ValidationError('两次密码不一致')
        attrs['password'] = make_password(attrs['password'])
        del attrs['pwd2']
        return attrs


class SigninSerializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=16, min_length=6)
    password = serializers.CharField(max_length=16, min_length=6)
    key = serializers.CharField(max_length=128, required=False, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'key')

    def validate(self, attrs):
        user = User.objects.filter(username=attrs['username']).first()
        if user:
            if check_password(attrs['password'], user.password):
                key = uuid.uuid4()
                Token.objects.update_or_create(defaults={'key': key}, user=user)
                attrs['key'] = key
                return attrs
        else:
            raise ValidationError('用户名或密码错误')
