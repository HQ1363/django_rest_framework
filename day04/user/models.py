from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=64)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
