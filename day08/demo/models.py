from django.db import models
from django.contrib.auth.models import AbstractUser, User


class Book(models.Model):
    name = models.CharField(max_length=20, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.CharField(max_length=20)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=256)
    tel = models.CharField(max_length=11)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
