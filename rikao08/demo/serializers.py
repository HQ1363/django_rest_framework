# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import uuid

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import check_password

from .models import User, Token, Dasha, Company


# 4.结合使用postman，完成用户登录，使用并配置TokenAuthentication生成或更新token表
class LoginSerializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=16, min_length=6)
    password = serializers.CharField(max_length=16, min_length=6)
    key = serializers.CharField(max_length=128, write_only=True, required=False)

    class Meta:
        model = User
        feilds = ('username', 'password', 'key')

    def validate(self, attrs):
        user = User.objects.filter(username=attrs['username']).first()
        if user:
            if check_password(attrs['password'], user.password):
                key = uuid.uuid4()
                Token.objects.update_or_create(defaults={'key': key}, user=user)
                attrs['key'] = key
                return attrs
            raise ValidationError('用户名或密码错误')


class CompanySerializers(serializers.ModelSerializer):
    # 外键要求使用PrimaryKeyRelatedField输出
    dasha = serializers.PrimaryKeyRelatedField(queryset=[Dasha.objects.all()])

    class Meta:
        model = Company
        feilds = '__all__'


class DashaSerializers(serializers.ModelSerializer):
    companys = CompanySerializers(many=True)
    louc = serializers.IntegerField()

    class Meta:
        model = Dasha
        feilds = '__all__'

    # 6.完成添加大厦信息功能，需要添加验证，大厦楼层高必须大于0
    def validate(self, attrs):
        if attrs['louc'] <= 0:
            raise ValidationError('大厦楼层高必须大于0')
        return attrs
