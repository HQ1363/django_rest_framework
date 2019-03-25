# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework import serializers
from .models import Class, Student


class ClsSerializers(serializers.ModelSerializer):
    students = serializers.HyperlinkedIdentityField(read_only=True, view_name='viewsetlearn:stusingle', many=True)

    class Meta:
        model = Class
        fields = '__all__'


class StuSerializers(serializers.ModelSerializer):
    age = serializers.IntegerField(max_value=99, min_value=1)
    gendrer = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Student
        fields = '__all__'

    # 重写create方法，修改validated_data中的键get_gender_display为数据库中字段gender
    def create(self, validated_data):
        validated_data['gender'] = validated_data['get_gender_display']
        del validated_data['get_gender_display']
        return Student.objects.create(**validated_data)

    # 修改instance.gender取值方法为获取get_gender_display的值
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('get_gender_display', instance.gender)
        instance.save()
        return instance
