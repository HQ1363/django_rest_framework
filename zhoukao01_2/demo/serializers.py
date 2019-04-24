# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework import serializers

from .models import Types, Goods


# 3.	新建序列化器，对商品表和分类表进行序列化输出
class GoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'


class TypesSerializers(serializers.ModelSerializer):
    # 4.    在序列化器中将分类表商品表进行嵌套序列化
    goods = GoodsSerializers(required=False, many=True)

    class Meta:
        model = Types
        fields = '__all__'
