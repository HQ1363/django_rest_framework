from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=64)
    tel = models.CharField(max_length=11)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username


class Code(models.Model):
    code = models.CharField(max_length=10)
    tel = models.CharField(max_length=11, unique=True)
    addtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'code'

    def __str__(self):
        return self.code


class Token(models.Model):
    token = models.CharField(max_length=128, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'token'

    def __str__(self):
        return self.user.username


class Type(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'type'

    def __str__(self):
        return self.name


class Goods(models.CharField):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='goods')
    name = models.CharField(max_length=20)
    price = models.FloatField(default=0.0)
    hot = models.CharField(choices=(('0', '不热销'), ('1', '热销')), max_length=1)

    class Meta:
        db_table = 'goods'

    def __str__(self):
        return self.name


class Order(models.Model):
    num = models.CharField(max_length=64)
    mount = models.FloatField(default=0.0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')

    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.user.username
