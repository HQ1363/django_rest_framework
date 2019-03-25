from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name


class Order(models.Model):
    code = models.CharField(max_length=20, unique=True)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order', to_field='name')

    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.code


class Type(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'type'

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_top = models.CharField(choices=(('0', '热销'), ('1', '非热销')), max_length=1)
    clicknum = models.IntegerField()
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='goods')
    order_id = models.ManyToManyField(Order, related_name='order')

    class Meta:
        db_table = 'goods'

    def __str__(self):
        return self.name
