from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=20, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.CharField(max_length=20)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name
