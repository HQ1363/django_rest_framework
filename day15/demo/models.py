from django.db import models
from django.contrib.auth.models import AbstractUser


class Code(models.Model):
    tel = models.CharField(max_length=11, unique=True)
    code = models.CharField(max_length=6)
    addtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'code'


class User(AbstractUser):
    tel = models.CharField(max_length=11, unique=True)
    age = models.IntegerField(default=18)
    is_staff = models.CharField(max_length=20, choices=(('1', '普通用户'), ('2', 'VIP用户'), ('3', 'SVIP用户')), default='1')

    class Meta:
        db_table = 'user'


class Token(models.Model):
    key = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='token')

    class Meta:
        db_table = 'token'


class Goods(models.Model):
    title = models.CharField(max_length=20)
    price = models.FloatField(default=0.0)

    class Meta:
        db_table = 'goods'
