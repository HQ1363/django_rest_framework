from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.IntegerField(default=1)
    tel = models.CharField(max_length=11)

    class Meta:
        db_table = 'user'


class Token(models.Model):
    key = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='token')

    class Meta:
        db_table = 'token'
