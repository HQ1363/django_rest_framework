# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User


class Registerserializers(serializers.ModelSerializer):
    # 需要添加password2 字段
    password2 = serializers.CharField(max_length=64, min_length=6, label='确认密码',
                                      error_messages={'max_length': '密码最多64位', 'min_length': '密码最少6位'})

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'username': {'max_length': 16,
                         'min_length': 6,
                         'label': '用户名',
                         'error_messages': {'max_length': '用户名最多16位', 'min_length': '用户名最少6位'}
                         },
            'password': {'max_length': 64,
                         'min_length': 6,
                         'label': '密码',
                         'error_messages': {'max_length': '密码最多64位', 'min_length': '密码最少6位'}}
        }

    def validate(self, attrs):
        if attrs['password2'] != attrs['password']:
            raise ValidationError('密码不一致')
        # models 中不需要保存password2，删除
        del attrs['password2']
        return attrs


class Loginserializers(serializers.ModelSerializer):
    # models中name有unique=True，自动生成的序列化器name字段，也具有唯一性验证，我们要重写，去掉唯一性验证
    username = serializers.CharField(max_length=16, min_length=6, label='用户名',
                                     error_messages={'max_length': '用户名最多16位', 'min_length': '用户名最少6位'})

    class Meta:
        model = User
        fields = '__all__'

    def validate_username(self, username):
        if not User.objects.filter(username=username).exists():
            raise ValidationError('用户名不存在')
        return username

    def validate(self, attrs):
        user = User.objects.get(username=attrs['username'])
        if attrs['password'] != user.password:
            raise ValidationError('密码错误')
        return attrs
