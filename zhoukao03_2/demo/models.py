from django.db import models


# 1.定义商品分类和商品模型类，关系为一对多
# 2.使用sql语句进行数据的导入
class Gtype(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'gtype'


# 1.定义商品分类和商品模型类，关系为一对多
# 2.使用sql语句进行数据的导入
class Goods(models.Model):
    title = models.CharField(max_length=40)
    price = models.FloatField(default=0.0)
    gtype = models.ForeignKey(Gtype, on_delete=models.CASCADE, related_name='goods')

    class Meta:
        db_table = 'goods'
