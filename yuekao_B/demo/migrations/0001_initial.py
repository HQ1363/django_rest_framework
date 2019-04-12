# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-07 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=255)),
                ('c_href', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='WineInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=255)),
                ('ex_tax', models.CharField(max_length=255)),
                ('producer', models.CharField(max_length=255)),
                ('grape', models.CharField(max_length=255)),
                ('awards', models.CharField(max_length=255)),
                ('notes', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'wineinfo',
            },
        ),
        migrations.CreateModel(
            name='WinePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_href', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winepage', to='demo.Country')),
            ],
            options={
                'db_table': 'winepage',
            },
        ),
        migrations.AddField(
            model_name='wineinfo',
            name='winepage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wineinfo', to='demo.WinePage'),
        ),
    ]
