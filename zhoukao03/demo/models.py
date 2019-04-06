from django.db import models
from django.contrib.auth.models import AbstractUser


# 2.	用户模型User， 继承Django的AbstractUser类，属性：住址，性别，手机号（必填项，唯一）
class User(AbstractUser):
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=(('0', '男'), ('1', '女')))
    phone = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username


# 7.	项目支持basic auth认证，定义token表
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='token')
    key = models.CharField(max_length=128)
    addtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'token'

    def __str__(self):
        return self.user.username


# 3.	定义短信验证码表，SmsCaptcha，包括验证码、手机号和添加时间（默认当前时间）
class SmsCaptcha(models.Model):
    code = models.CharField(max_length=6)
    tel = models.CharField(max_length=11, unique=True)
    addtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'smscaptcha'

    def __str__(self):
        return self.code
