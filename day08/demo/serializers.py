# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
import uuid
from .models import Book, User


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class RegisterSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=16, min_length=6, write_only=True)
    password = serializers.CharField(max_length=16, min_length=6)
    tel = serializers.CharField(max_length=11, min_length=11)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'tel')

    # 验证两次密码是否一致
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError('两次密码不一致')
        return attrs

    def create(self, validated_data):
        pwd = validated_data.get('password')
        # 删除pwd2字段，数据表中没有该字段
        del validated_data['password2']
        # 创建用户
        user = User.objects.create(**validated_data)
        # 修改用户密码为加密后密码
        user.set_password(pwd)
        user.save()
        return user


class LoginSerializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=16, min_length=6)
    # required=False前端不必须传入token字段，write_only=True不需要从数据库读取这个字段
    token = serializers.CharField(max_length=40, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'token')

    def validate(self, attrs):
        if not User.objects.filter(username=attrs['username']).exists():
            raise ValidationError('用户名不存在')
        else:
            user = User.objects.get(username=attrs['username'])
            if not user.check_password(attrs['password']):
                raise ValidationError('密码错误')
        # 获取加密字符串key，加密后最大长多40，选择加密方法要注意长度
        key = uuid.uuid4()
        # defaults字典,放要更新字段.    user=user_obj,指定查询字段为user
        # Token.objects.update_or_create(defaults={'key': key}, user=user)
        token = Token.objects.filter(user=user)
        if token:
            token.update(key=key)
        else:
            token.create(user=user, key=key)
        attrs['token'] = key
        return attrs
