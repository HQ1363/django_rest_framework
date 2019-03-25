from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from .models import Class, Student
from .serializers import ClsSerializers, StuSerializers


# 提供全部方法
class StuViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StuSerializers


# 只提供list，retrieve方法
class StuShow(ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StuSerializers


# 自定义继承viewset
class MyStu(mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StuSerializers


class ClsViewset(ReadOnlyModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClsSerializers
