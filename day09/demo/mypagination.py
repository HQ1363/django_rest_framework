# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework.pagination import PageNumberPagination


class MyPage(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'ps'
    max_page_size = 5
