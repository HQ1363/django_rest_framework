# -*- coding: utf-8 -*-
# -*- author: GXR -*-

from rest_framework.pagination import PageNumberPagination


# 对接口添加分页功能，实现自定义分页
class Mypagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    page_size_query_param = 'ps'
    max_page_size = 5
