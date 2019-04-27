from django.contrib import admin

from .models import Gtype, Goods


# 1.将模型类注册到admin后台
@admin.register(Gtype)
class GtypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


# 1.将模型类注册到admin后台
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'gtype']
