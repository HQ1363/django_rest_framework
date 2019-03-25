# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework import serializers
from .models import StuClass, Student


class ClaSerializers(serializers.ModelSerializer):
    class Meta:
        model = StuClass  # 指定对应的模型类
        fields = '__all__'  # 指定显示字段，’__all__‘,全部显示


class StuSerializers(serializers.ModelSerializer):
    cls = serializers.PrimaryKeyRelatedField(queryset=StuClass.objects.all())

    class Meta:
        model = Student
        fields = "__all__"
