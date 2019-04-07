# -*- coding: utf-8 -*-
# -*- author: GXR -*-
import re
import uuid
from datetime import datetime, timedelta

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from django.db.models.query_utils import Q

from .models import User, Token, SmsCaptcha

tel_re = r'1[356789]\d{9}'


# 4.完成短信发送接口，集成第三方服务（如云片），发送短信需要判断手机号是否合法、判断同一个手机号一分钟内最多发送一次短信，否则给出对应信息
class SmsCaptchaSerializers(serializers.ModelSerializer):
    tel = serializers.CharField(max_length=11, min_length=11)

    class Meta:
        model = SmsCaptcha
        fields = ('tel',)

    def validate(self, attrs):
        if not re.match(tel_re, attrs['tel']):
            raise ValidationError('手机号不合法')
        # 一分钟之前时间
        one_m_ago = datetime.now() - timedelta(minutes=1)
        if SmsCaptcha.objects.filter(tel=attrs['tel'], addtime__gt=one_m_ago).count():
            raise ValidationError('同一个手机号一分钟内最多发送一次短信')
        return attrs


# 5.定义用户注册页面（包含：用户名，手机号，密码，住址，性别等元素），ajax异步提交注册信息，验证通过后，提示注册成功
# 6.注册时，需判断：短信验证码是否正确，用户名和手机号是否重复，同一手机号1分钟内最多发送1次短信，短信验证码是否过期（设置90秒过期）
class RegisterSerializers(serializers.ModelSerializer):
    pwd2 = serializers.CharField(max_length=128, min_length=6, write_only=True)
    password = serializers.CharField(max_length=128, min_length=6)
    gender = serializers.CharField(source='get_gender_display')
    code = serializers.CharField(max_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'address', 'gender', 'phone', 'pwd2', 'code')

    def validate(self, attrs):
        if attrs['password'] != attrs['pwd2']:
            raise ValidationError('两次密码不一致')
        s90_ago = datetime.now() - timedelta(seconds=90)
        if not SmsCaptcha.objects.filter(tel=attrs['phone'], code=attrs['code']).count():
            raise ValidationError('验证码错误')
        if SmsCaptcha.objects.filter(tel=attrs['phone'], addtime__lt=s90_ago).count():
            raise ValidationError('验证码失效')
        attrs['password'] = make_password(attrs['password'])
        attrs['gender'] = attrs['get_gender_display']
        del attrs['code']
        del attrs['pwd2']
        del attrs['get_gender_display']
        return attrs


# 8.完成用户登录功能，用户的手机号和密码登录，登录成功生成token存库
class LoginSerializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=16, min_length=6)
    password = serializers.CharField(max_length=16, min_length=6)
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


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
