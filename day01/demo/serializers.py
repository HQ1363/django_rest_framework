# -*- coding: utf-8 -*-
# -*- author: GXR -*-

# 序列化是将数据对象转换为前端需要的数据类型（一般json格式）的过程，发送给前端
# 反序列化就是将前端发送过来的数据转换为数据对象，方便对数据操作

from rest_framework import serializers
from .models import Student


# 序列化器
class StuSerializers(serializers.Serializer):
    # 需要序列化的字段名
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField(min_value=0, max_value=99)
    gender = serializers.IntegerField()

    # 创建新对象时，需要重写create方法
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # 修改对象时，需要重写update方法
    def update(self, instance, validated_data):
        # param-instance: 数据对象
        # param-validated_data: 经过合法性验证的前端发送过来的数据
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance
