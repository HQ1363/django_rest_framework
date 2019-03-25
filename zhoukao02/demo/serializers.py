# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework import serializers
from .models import Company, Employee


class EmpSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


# 4.	使用serialize完成使用公司和员工的嵌套序列化输出
class ComSerializers(serializers.ModelSerializer):
    employee = EmpSerializers(many=True)

    class Meta:
        model = Company
        fields = '__all__'
