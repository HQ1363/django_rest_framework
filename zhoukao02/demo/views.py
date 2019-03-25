from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from .models import Company, Employee
from .serializers import ComSerializers, EmpSerializers


# 3.	创建公司的API接口
class ComList(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = ComSerializers
    # 9.给接口加上basic认证
    authentication_classes = (BasicAuthentication,)


# 5.	修改和删除公司信息API接口
class ComSingle(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = ComSerializers
    # 9.给接口加上basic认证
    authentication_classes = (BasicAuthentication,)


# 创建员工信息API接口
class EmpList(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializers
    # 9.给接口加上basic认证
    authentication_classes = (BasicAuthentication,)


# 6.	修改和删除员工信息API接口
class EmpSingle(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializers
    # 9.给接口加上basic认证
    authentication_classes = (BasicAuthentication,)
