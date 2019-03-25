# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework import serializers
from .models import Type, Goods


class Typeserializers(serializers.ModelSerializer):
    class Meta:
        model = Type
        # 指定字段
        fields = ('name',)


class Goodsserializers(serializers.ModelSerializer):
    # 每种商品只对应一种类型，不用many=True
    type_id = Typeserializers()

    class Meta:
        model = Goods
        # 所有字段
        fields = '__all__'
        # 指定只读字段
        # read_only_fields = ()
        # 指明不需要的字段
        # exclude = ()
        # 为字段添加额外参数
        extra_kwargs = {'name': {'min_length': 10, 'label': '名字'}}


class TySerializers(serializers.ModelSerializer):
    # 每种类型有多种商品，需要many=True
    goods = Goodsserializers(many=True)

    class Meta:
        model = Goods
        fields = ('name', 'price')
