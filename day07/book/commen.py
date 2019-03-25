# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import FilterSet, filters
from .models import Book


class Bookpaginations(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    page_size_query_param = 'ps'
    max_page_size = 5


class Bookfilters(FilterSet):
    gte_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    lte_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Book
        fields = '__all__'
