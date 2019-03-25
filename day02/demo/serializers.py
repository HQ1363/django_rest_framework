# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from .models import Class, Student


def validator_name(name):
    if Student.objects.get(name=name):
        raise ValidationError('名字已存在！！！')
    return name


class ClsSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=255, validators=[UniqueValidator(queryset=Class.objects.all())])
    num = serializers.IntegerField(min_value=13, max_value=50)


class StuSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=False)
    # validators 验证，传入验证函数名称，不用()
    # 验证年龄是不是唯一
    age = serializers.IntegerField(min_value=1, max_value=99, required=False,
                                   validators=[UniqueValidator(queryset=Student.objects.all())])
    gender = serializers.ChoiceField(choices=[0, 1], required=False)
    # 外键关联序列化
    class_id = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())

    class Meta:
        # 验证联合唯一
        validators = [
            UniqueTogetherValidator(
                queryset=Student.objects.all(),
                fields=('name', 'gender'))
        ]

    # 新建数据时，必须重写
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.class_id = validated_data.get('class_id', instance.class_id)
        instance.save()
        return instance

    # validate_字段名称，对单一字段进行验证
    def validate_name(self, name):
        if len(name) > 5:
            raise ValidationError('名字太长！！！')
        return name

    # 可以对多个字段进行验证
    def validate(self, list):
        if list['gender'] == 1 and list['age'] > 30:
            raise ValidationError("老娘们儿不要！！！")
        # 需要返回值，验证通过的数值
        return list
