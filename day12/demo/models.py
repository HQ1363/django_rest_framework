from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=16, unique=True)
    tel = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = 'user'


class Code(models.Model):
    code = models.CharField(max_length=6)
    tel = models.CharField(max_length=11, unique=True)
    addtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'code'
