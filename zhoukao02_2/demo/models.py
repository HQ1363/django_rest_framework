from django.db import models


# 定义学生和班级模型类，关系为一对多
class Stuclass(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'stuclass'


# 使用sql语句进行数据的导入
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)
    cls = models.ForeignKey(Stuclass, on_delete=models.CASCADE, related_name='students')

    class Meta:
        db_table = 'student'
