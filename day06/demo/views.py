from rest_framework.viewsets import ViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Class, Student
from .serializers import StudnetSerializers, ClassSerializers
from .pagenations import Stupagenations, Stulimit
from .filters import Stufilter


class Stulist(ListCreateAPIView):
    # 自定义分页，APIView中没有pagination_class 属性
    pagination_class = Stupagenations
    # pagination_class = Stulimit

    # 指定单个视图的过滤
    # filter_backends = (DjangoFilterBackend,)
    # 指定过滤字段
    # filter_fields = ('name', 'num')
    # 指定过滤类为自定义过滤类
    filter_class = Stufilter
    # 注意为元组，单个的时候加逗号
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    search_fields = ('=name', 'class_id')
    ordering_fields = ('num', 'class_id', 'name')
    ordering = ('name', 'class_id')
    '''
        可以通过在search_fields前面添加各种字符来限制搜索行为。
        '^' 以指定内容开始.
        '=' 完全匹配
        '@' 全文搜索（目前只支持Django的MySQL后端）
        '$' 正则搜索
        例如：
        search_fields = ('=username', '=email')
    '''
    queryset = Student.objects.all()
    serializer_class = StudnetSerializers


class Stusingle(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudnetSerializers


class Clslist(ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializers


class Clssingle(RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializers
