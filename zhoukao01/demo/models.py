from django.db import models


# 2.	班级模型StuClass,班级名称, 班级号（唯一约束）; 学生模型Student，模型属性有: 学号(唯一约束),学生名称,年龄,性别，模型关系 1班级：n学生（5分）

class StuClass(models.Model):
    clsname = models.CharField(max_length=20, verbose_name='班级名称')
    clsnum = models.CharField(max_length=20, verbose_name='班级号', unique=True)

    class Meta:
        db_table = 'stuclass'

    def __str__(self):
        return self.clsname


class Student(models.Model):
    stunum = models.CharField(max_length=20, verbose_name='学号', unique=True)
    name = models.CharField(max_length=20, verbose_name='名称')
    age = models.CharField(max_length=2, verbose_name='年龄')
    gender = models.CharField(choices=(('0', 'man'), ('1', 'women')), max_length=1, verbose_name='性别')
    cls = models.ForeignKey(StuClass, on_delete=models.CASCADE, verbose_name='所属班级')

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.name
