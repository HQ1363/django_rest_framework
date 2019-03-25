from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=64)
    phone = models.CharField(max_length=11)

    class Meta:
        db_table = 'userinfo'

    def __str__(self):
        return self.username
