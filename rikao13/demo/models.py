from django.db import models


class Code(models.Model):
    tel = models.CharField(max_length=11, unique=True)
    code = models.CharField(max_length=6)
    addtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'code'
