# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-06 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20190505_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('price', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
    ]