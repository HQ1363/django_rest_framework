from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Company, Employee
from .serializers import ComSerializers, EmpSerializers


# 3.	创建公司的API接口
class CompanyShow(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = ComSerializers
    # 分页
    # pagination_class = Mypagination
    # 9.给接口加上basic认证
    authentication_classes = (BasicAuthentication,)
    # 权限
    permission_classes = (IsAuthenticated,)


# 创建员工信息API接口
class EmployeeShow(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializers
    # 分页
    # pagination_class = Mypagination
    # 9.给接口加上basic认证
    authentication_classes = (BasicAuthentication,)
    # 权限
    permission_classes = (IsAuthenticated,)
