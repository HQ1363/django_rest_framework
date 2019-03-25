from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'class'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(choices=(('0', '男'), ('1', '女')), max_length=1)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.name
