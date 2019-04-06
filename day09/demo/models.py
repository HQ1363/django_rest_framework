from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20, unique=True)
    pwd = models.CharField(max_length=128)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name


class Token(models.Model):
    token = models.CharField(max_length=128, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'token'

    def __str__(self):
        return self.user.name
