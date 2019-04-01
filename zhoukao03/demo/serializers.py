# -*- coding: utf-8 -*-
# -*- author: GXR -*-
import re
import uuid
from datetime import datetime, timedelta

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Token, SmsCaptcha

tel_re = r'1[35789]\d{9}'


# 4.完成短信发送接口，集成第三方服务（如云片），发送短信需要判断手机号是否合法、判断同一个手机号一分钟内最多发送一次短信，否则给出对应信息
class SmsCaptchaSerializers(serializers.ModelSerializer):
    class Meta:
        model = SmsCaptcha
        fields = '__all__'

    def validate(self, attrs):
        if not re.match(attrs['tel'], tel_re):
            raise ValidationError('手机号不合法')
        one_m_ago = datetime.now() - timedelta(minutes=1)
        if datetime.now() - one_m_ago >= 60:
            raise ValidationError('同一个手机号一分钟内最多发送一次短信')
        else:
            addtime = one_m_ago
            SmsCaptcha.objects.update_or_create(code=attrs['code'], tel=attrs['tel'], addtime=addtime)
            return attrs


# 5.定义用户注册页面（包含：用户名，手机号，密码，住址，性别等元素），ajax异步提交注册信息，验证通过后，提示注册成功
# 6.注册时，需判断：短信验证码是否正确，用户名和手机号是否重复，同一手机号1分钟内最多发送1次短信，短信验证码是否过期（设置90秒过期）
class RegisterSerializers(serializers.ModelSerializer):
    code = serializers.CharField(max_length=6, min_length=6)
    password = serializers.CharField(max_length=128, min_length=6)
    pwd2 = serializers.CharField(max_length=128, min_length=6)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        if attrs['password'] != attrs['pwd2']:
            raise ValidationError('两次密码不一致')
        code = SmsCaptcha.objects.filter(code=attrs['code']).first()
        if code:
            m_ago = datetime.now() - timedelta(seconds=90)
            if m_ago > code.addtime:
                raise ValidationError('短信验证码过期')
            if attrs['code'] != code.code:
                raise ValidationError('短信验证码错误')
        del attrs['code']
        del attrs['pwd2']
        return attrs

    def create(self, validated_data):
        validated_data['passdword'] = make_password(validated_data['passdword'])
        return User.objects.create(**validated_data)


# 8.完成用户登录功能，用户的手机号和密码登录，登录成功生成token存库
class LoginSerializers(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=11, min_length=11)
    password = serializers.CharField(max_length=128, min_length=6)

    class Meta:
        model = User
        fields = ('phone', 'password')

    def validate(self, attrs):
        user = User.objects.filter(phone=attrs['phone']).first
        if user:
            if check_password(user.password, attrs['password']):
                key = uuid.uuid4()
                user = user.save()
                Token.objects.update_or_create(defaults={'key': key, 'user': user})
                return attrs
        raise ValidationError('手机号或密码错误l')


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
