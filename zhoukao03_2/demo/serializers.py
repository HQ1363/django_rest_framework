# -*- coding: utf-8 -*-
# -*- author: GXR -*-

from rest_framework import serializers

from .models import Gtype, Goods


# 4.完成商品分类和商品表的序列化，并且进行嵌套序列化输出
class GoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'


# 4.完成商品分类和商品表的序列化，并且进行嵌套序列化输出
class GtypeSerializers(serializers.ModelSerializer):
    goods = GoodsSerializers(many=True)

    class Meta:
        model = Gtype
        fields = '__all__'
