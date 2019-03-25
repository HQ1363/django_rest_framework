from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=255, verbose_name='班级')
    num = models.IntegerField(verbose_name='班级号')

    class Meta:
        db_table = 'class'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    gender = models.IntegerField(choices=((0, 'man'), (1, 'women')), verbose_name='性别')
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.name
