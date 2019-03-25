# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework import serializers
from .models import Type, Goods
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator


class Typeserializers(serializers.Serializer):
    name = serializers.CharField(max_length=20,
                                 validators=[UniqueValidator(queryset=Type.objects.all(), message='已存在该类型')],
                                 label='类型')


class Goodsserializers(serializers.Serializer):
    # read_only为True时，该字段只能用于序列化输出，不能用于反序列化，也就是只能在页面上看到，不能对他进行修改
    # type_id = serializers.PrimaryKeyRelatedField(read_only=True)

    # 想要修改的化，需要设置queryset查询集,页面显示id
    # type_id = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())

    # 显示详细信息
    # type_id = Typeserializers()

    # 显示指定字段, 根据models中定义的__str__方法返回
    type_id = serializers.StringRelatedField()

    name = serializers.CharField(max_length=20, label='商品')
    # error_messages报错信息，字典形式
    price = serializers.DecimalField(max_digits=6, decimal_places=2,
                                     error_messages={'max_digits': '价格错误', 'decimal_places': '价格错误'})

    # 联合唯一验证
    class Meta:
        validators = [UniqueTogetherValidator(queryset=Goods.objects.all(), fields=('name', 'price'))]

    # 对字段进行验证
    def validate_name(self, name):
        if Goods.objects.filter(name=name).exists():
            raise ValidationError('名字已存在')
        return name

    # 对多个字段进行验证
    def validate(self, attrs):
        if Goods.objects.filter(name=attrs['name']).exists():
            raise ValidationError('名字已存在')
        if attrs['price'] <= 0:
            raise ValidationError('价格错误')
        return attrs

    def create(self, validated_data):
        return Goods.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # type要修改的数据赋值给type_data
        typa_data = validated_data.pop('type_id')

        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        # instance.type_id = validated_data.get('type_id', instance.type_id)
        instance.save()
        # 根据外键，获取ype对象
        type = instance.type_id
        # 修改名字
        type.name = typa_data.get('name', type.name)
        # 修改完成，保存
        type.save()
        return instance


class TySerializers(serializers.Serializer):
    name = serializers.CharField(max_length=20,
                                 validators=[UniqueValidator(queryset=Type.objects.all(), message='已存在该类型')],
                                 label='类型')
    # goods = serializers.SlugRelatedField(queryset=Goods.objects.all(),slug_field='name',many=True)
    goods = Goodsserializers(many=True)
