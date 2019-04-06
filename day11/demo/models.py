from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    tel = models.CharField(max_length=11)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username


class Student(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age = models.IntegerField()

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.name
