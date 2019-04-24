from django.db import models
from django.contrib.auth.models import AbstractUser


class Code(models.Model):
    tel = models.CharField(max_length=11, unique=True)
    code = models.CharField(max_length=6)

    class Meta:
        db_table = 'code'


class User(AbstractUser):
    tel = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = 'user'


class Token(models.Model):
    key = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='token')
    addtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'token'
