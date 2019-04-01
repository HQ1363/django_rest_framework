# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework.pagination import PageNumberPagination


class Mypagination(PageNumberPagination):
    page_size_query_param = 'ps'
    page_query_param = 'p'
    page_size = 2
    max_page_size = 5
