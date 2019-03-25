# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import ValidationError
from .models import UserInfo
import re

p = r'1[35678]\d{9}'


class UserSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=16, min_length=6,
                                     validators=[UniqueValidator(queryset=UserInfo.objects.all(), message='已存在该用户名')])
    password = serializers.CharField(max_length=64, min_length=6)
    phone = serializers.CharField(max_length=11, min_length=11)

    def validate_phone(self, phone):
        if not re.match(p, phone):
            raise ValidationError('手机号格式不对')
        return phone

    def create(self, validated_data):
        return UserInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance


class UserModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('username', 'password', 'phone')
        extra_kwargs = {
            'username': {'min_length': 6},
            'password': {'min_length': 6},
            'phone': {'min_length': 11}
        }

    def validate_phone(self, phone):
        if not re.match(p, phone):
            raise ValidationError('手机号格式不对')
        return phone
