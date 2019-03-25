# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework import serializers
from .models import Type, Goods


class TypeSerializers(serializers.ModelSerializer):
    # 超链接：serializers.HyperlinkedRelatedField,主路由定义namespace,子路由定义name,view_name = 'namespacce:name'
    name = serializers.CharField(max_length=20)
    goods = serializers.HyperlinkedIdentityField(read_only=True, view_name='demo:goodsingle', many=True)

    class Meta:
        model = Type
        fields = '__all__'


class Goodserizlizers(serializers.ModelSerializer):
    type_id = TypeSerializers()

    class Meta:
        model = Goods
        fields = '__all__'

    def create(self, validated_data):
        type_data = validated_data.pop('type_id')
        # 判断类型是否存在，决定是否新建类型
        if not Type.objects.filter(name=type_data['name']).exists():
            # 类型不存在，新建
            type = Type.objects.create(**validated_data)
        else:
            # 类型已存在，获取类型
            type = Type.objects.get(name=type_data['name'])
        return Goods.objects.create(type_id=type, **validated_data)

    # 嵌套序列化，重写update方法
    def update(self, instance, validated_data):
        type_data = validated_data.pop('type_id')
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        type = instance.type_id
        type.name = type_data.get('name', type.name)
        type.save()
        return instance
