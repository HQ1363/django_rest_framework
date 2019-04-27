from django.contrib import admin

from .models import *


@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ['id', 'username']
