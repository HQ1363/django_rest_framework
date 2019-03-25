# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from django_filters.rest_framework import FilterSet
import django_filters
from .models import Student


# 自定义过滤，只有添加额外过滤字段，制定过滤规则才需要自定义
class Stufilter(FilterSet):
    # 添加gte_numb 过滤字段，指定过滤字段'num',过滤规则 gte大于等于
    gte_num = django_filters.NumberFilter(field_name='num', lookup_expr='gte')
    # 添加lte_numb 过滤字段，指定过滤字段'num',过滤规则 lte小于等于
    lte_num = django_filters.NumberFilter(field_name='num', lookup_expr='lte')
    class_name = django_filters.CharFilter(field_name='class_id__name')

    class Meta:
        # 指定对应模型类
        model = Student
        # 对全部字段过滤
        # fields = '__all__'
        # 指定过滤字段
        fields = ('class_name',)
