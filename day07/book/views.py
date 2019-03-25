from rest_framework.viewsets import ViewSet
from rest_framework.generics import ListCreateAPIView
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import Bookserializers
from .commen import Bookpaginations, Bookfilters


class Booklist(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializers
    pagination_class = Bookpaginations
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # 指定自定义过滤类
    filter_class = Bookfilters
    # 没有指定过滤类，需要指定过滤字段
    filter_fields = ('name', 'price')
    search_fields = ('name', '=price', 'author')
    ordering_fields = ('name', 'price')
    # 默认排序
    ordering = ('name', 'price')
