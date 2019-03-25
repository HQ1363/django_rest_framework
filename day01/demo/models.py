from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255, null=False)
    age = models.IntegerField()
    gender = models.IntegerField(choices=((0, 'man'), (1, 'women')))

    # 对数据表进行管理，重新命名
    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.name
