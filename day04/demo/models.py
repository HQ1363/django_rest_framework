from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'type'

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=20, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='goods')

    class Meta:
        db_table = 'goods'

    def __str__(self):
        return self.name
