from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import StudentSerializers, StuclassSerializers
from .models import Stuclass, Student
from .mypagination import Mypagination


# 对代码进行注释，并全程需要有调试的过程

# 视图需要使用viewset以及router
class StuclassShow(ModelViewSet):
    queryset = Stuclass.objects.all()
    serializer_class = StuclassSerializers
    # 对接口添加分页功能，实现自定义分页
    pagination_class = Mypagination


# 给接口添加增删改查功能，这里需要使用mixin
class StudentShow(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # 对接口添加过滤功能，例如进行年龄的过滤
    filter_fields = ['age']
    # 对接口添加搜索功能，例如进行姓名的搜索
    search_fields = ['name']
    # 对接口添加排序的功能，可以对年龄或者导入时间进行排序
    ordering_fields = ['age']
    ordering = ['age']
    # 对接口添加分页功能，实现自定义分页
    pagination_class = Mypagination
