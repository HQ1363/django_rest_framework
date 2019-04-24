# -*- coding: utf-8 -*-
# -*- author: GXR -*-

from rest_framework import serializers

from .models import *


# 完成学生表和班级的序列化
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


# 并且进行嵌套序列化输出
class StuclassSerializers(serializers.ModelSerializer):
    students = StudentSerializers(many=True, required=False)

    class Meta:
        model = Stuclass
        fields = '__all__'
