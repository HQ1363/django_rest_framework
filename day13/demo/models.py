from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=16, unique=True)
    tel = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = 'user'


class Token(models.Model):
    key = models.CharField(max_length=128, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='token')

    class Meta:
        db_table = 'token'


class Telcode(models.Model):
    tel = models.CharField(max_length=11)
    code = models.CharField(max_length=6)
    addtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'telcode'


class GoodsType(models.Model):
    type_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'goodstype'


class Goods(models.Model):
    name = models.CharField(max_length=20, unique=True)
    price = models.FloatField()
    is_hot = models.CharField(choices=(('0', '不热销'), ('1', '热销')), max_length=1)
    type_id = models.ForeignKey(GoodsType, on_delete=models.CASCADE, related_name='goods_type')

    class Meta:
        db_table = 'goods'


class Order(models.Model):
    code = models.CharField(max_length=128, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order')
    goods_id = models.ManyToManyField(Goods, related_name='goods_order')

    class Meta:
        db_table = 'order'
