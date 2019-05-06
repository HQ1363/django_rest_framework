# -*- coding: utf-8 -*-
# -*- author: GXR -*-
import django_filters

from .models import Goods


class Myfilter(django_filters.rest_framework.FilterSet):
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gt')

    class Meta:
        model = Goods
        fields = ('max_price', 'min_price')
