# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User, Type, Goods, Order


class Userserializers(serializers.Serializer):
    name = serializers.CharField(max_length=10, validators=[UniqueValidator(queryset=User.objects.all())])


class Orderserializers(serializers.Serializer):
    code = serializers.CharField(max_length=10, validators=[UniqueValidator(queryset=Order.objects.all())])
    total = serializers.DecimalField(max_digits=6, decimal_places=2)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.code = validated_data.get('code', instance.code)
        instance.total = validated_data.get('total', instance.total)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance


class Typeserializers(serializers.Serializer):
    name = serializers.CharField(max_length=10, validators=[UniqueValidator(queryset=Type.objects.all())])


# 重写to_representation()方法,序列化器的每个字段其实都是都是有该字段类型的to_representation来决定的,我们重写他.
class TypeRelated(serializers.RelatedField):
    # 自定义用于处理分类的字段
    def to_representation(self, value):
        return '所属分类：%s' % value.name


class Goodserializers(serializers.Serializer):
    name = serializers.CharField(max_length=10, validators=[UniqueValidator(queryset=Goods.objects.all())])
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    # is_top = serializers.ChoiceField(choices=(('0', '热销'), ('1', '非热销')))
    is_top = serializers.CharField(source='get_is_top_display')
    clicknum = serializers.IntegerField()
    type_id = TypeRelated(read_only=True)
    order_id = Orderserializers(many=True)
