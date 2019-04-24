from django.db import models
from django.contrib.auth.models import AbstractUser


# 1.定义用户表，继承AbstractUser，包括性别和手机号（5分）
# 2.定义大厦表，包括大厦名、大厦地址、大厦楼层高和是否有停车场字段（5分）
# 3.定义公司表，包括公司名、公司所属行业（要求使用choice，包括教育行业、计算机行业和医疗行业等）、是否上市以及注册资本（只填数字即可，单位是万人民币），并和大厦表进行一对多关联

class User(AbstractUser):
    gender = models.CharField(choices=(('0', '男'), ('1', '女')), max_length=1)
    phone = models.CharField(max_length=11)

    class Meta:
        db_table = 'user'


class Token(models.Model):
    key = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='token')

    class Meta:
        db_table = 'token'


class Dasha(models.Model):
    name = models.CharField(max_length=20)
    addr = models.CharField(max_length=90)
    # 楼层高，默认1层
    louc = models.IntegerField(default=1)
    # 0没有停车场，1有停车场，默认没有
    is_ting = models.IntegerField(default=0)

    class Meta:
        db_table = 'dasha'


class Company(models.Model):
    name = models.CharField(max_length=20)
    types = models.CharField(choices=(('0', '教育行业'), ('1', '计算机行业'), ('2', '医疗行业')), max_length=1)
    # 0没有上市，1上市，默认没有
    is_shang = models.IntegerField(default=0)
    money = models.FloatField()
    dasha = models.ForeignKey(Dasha, on_delete=models.CASCADE, related_name='companys')

    class Meta:
        db_table = 'company'
