# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class Stupagenations(PageNumberPagination):
    # 每页几条数据
    page_size = 3
    # 查询第几页的参数
    page_query_param = 'p'
    # 查询每页显示几条数据的参数
    page_size_query_param = 'ps'
    # 每页最多显示几条
    max_page_size = 5


class Stulimit(LimitOffsetPagination):
    # 每页几条数据
    default_limit = 2
    # 查询每页几条数据的参数
    limit_query_param = 'lim'
    # 查询跳过几条数据的参数
    offset_query_param = 'off'
    # 每页最多几条数据
    max_limit = 4
