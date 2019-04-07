from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=128)
    tel = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = 'user'


class Token(models.Model):
    key = models.CharField(max_length=128, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='token')

    class Meta:
        db_table = 'token'


class Code(models.Model):
    code = models.CharField(max_length=6)
    tel = models.CharField(max_length=11, unique=True)
    addtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'code'


class Guoji(models.Model):
    name = models.CharField(max_length=255)
    miaoshu = models.CharField(max_length=255)
    miaosu = models.CharField(max_length=255)
    xianjia = models.CharField(max_length=255)
    yuanjia = models.CharField(max_length=255)
    guojia = models.CharField(max_length=255)
    yishou = models.CharField(max_length=255)
    shangpinid = models.CharField(max_length=255)
    img_src = models.CharField(max_length=255)

    class Meta:
        db_table = 'guoji'
