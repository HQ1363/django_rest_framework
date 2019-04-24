from django.db import models


# 1.	定义商品和分类两张表，进行一对多关联
class Types(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'types'

    def __str__(self):
        return self.name


class Goods(models.Model):
    title = models.CharField(max_length=20)
    price = models.FloatField(default=0.0)
    types = models.ForeignKey(Types, on_delete=models.CASCADE, related_name='goods')

    class Meta:
        db_table = 'goods'

# 2.	使用sql语句导入数据，这里使用图形化工具或者使用后台管理系统导入数据不给分
