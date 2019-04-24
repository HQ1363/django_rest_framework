from django.contrib import admin

from .models import *


# 将模型类注册到admin后台
@admin.register(Stuclass)
class StuclassAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'cls']
