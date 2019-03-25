from django.db import models


# 2.	公司模型Company：公司名称（唯一约束）; 员工模型Employee: 工号(唯一约束),员工名称,年龄,性别，模型关系 1公司：n员工

class Company(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'company'

    def __str__(self):
        return self.name


class Employee(models.Model):
    num = models.IntegerField(unique=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(choices=(('0', '男'), ('1', '女')), max_length=1)
    com_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employee')

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.name
