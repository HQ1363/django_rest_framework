# -*- coding: utf-8 -*-
# -*- author: GXR -*-
import uuid

from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.exceptions import ValidationError

from .models import User, Token


class RegisterSerializers(serializers.ModelSerializer):
    pwd = serializers.CharField(max_length=128, min_length=6)
    pwd2 = serializers.CharField(max_length=128, min_length=6)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'name': {'min_length': 6}
        }

    def validate(self, attrs):
        if attrs['pwd'] != attrs['pwd']:
            raise ValidationError('两次密码不一致')
        del attrs['pwd2']
        return attrs

    def create(self, validated_data):
        validated_data['pwd'] = make_password(validated_data['pwd'])
        return User.objects.create(**validated_data)


class LoginSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=16)
    token = serializers.CharField(max_length=40, required=False, write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        user = User.objects.filter(name=attrs['name']).first()
        if user:
            if check_password(attrs['pwd'], user.pwd):
                token = uuid.uuid4()
                Token.objects.update_or_create(defaults={'token': token}, user=user)
                attrs['token'] = token
                return attrs
        raise ValidationError('用户名或密码错误')


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
