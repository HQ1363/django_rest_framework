# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework import serializers
from .models import Class, Student


class StudnetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ClassSerializers(serializers.ModelSerializer):
    # 主表下包含多条副表数据
    students = StudnetSerializers(many=True)

    class Meta:
        model = Class
        fields = '__all__'

    def update(self, instance, validated_data):
        stu_data = validated_data.pop('student')
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        stu = Student.objects.filter(name=stu_data[0]['name']).first()
        stu.num = stu_data[0]['num']
        stu.name = stu_data[0]['name']
        stu.gender = stu_data[0]['gender']
        stu.class_id = stu_data[0]['class_id']
        stu.save()
        return instance
