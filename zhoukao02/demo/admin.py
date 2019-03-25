from django.contrib import admin
from .models import Company, Employee


# 11.	创建超级用户，公司和员工模型注册到admin后台，所有字段均展示

@admin.register(Company)
class ComAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Employee)
class EmpAdmin(admin.ModelAdmin):
    list_display = ['num', 'name', 'age', 'gender', 'com_id']
