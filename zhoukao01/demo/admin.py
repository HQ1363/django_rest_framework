from django.contrib import admin
from .models import StuClass, Student


# 11.	创建超级用户，学生和班级模型注册到admin后台，所有字段均展示
@admin.register(StuClass)
class StuclassAdmin(admin.ModelAdmin):
    list_display = ['clsname', 'clsnum']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['stunum', 'name', 'age', 'gender', 'cls']
