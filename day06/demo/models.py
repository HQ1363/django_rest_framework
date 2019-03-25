from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'class'

    def __str__(self):
        return self.name


class Student(models.Model):
    num = models.IntegerField(unique=True)
    name = models.CharField(max_length=20)
    gender = models.CharField(choices=(('0', 'man'), ('1', 'women')), max_length=1)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.name
