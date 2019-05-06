from yunpian import YunPian
import uuid

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, AllowAny
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import CodeSerializers, SignUpSerializers, SignInSerializers, GoodsSerializers
from .models import Code, User, Token, Goods
from .myauthentication import MyToken
from .mypermissions import MyPermissions, UserPermissions
from .myfilter import Myfilter
from .myerror import MyError


class CodeShow(ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializers

    def create(self, request, *args, **kwargs):
        ser = CodeSerializers(data=request.data)
        if ser.is_valid():
            yun = YunPian()
            code = yun.make_code()
            res = yun.send_code(ser.validated_data['tel'], code)
            if res['code'] != 0:
                return Response({
                    'msg': res['msg'],
                    'code': 1000
                })
            else:
                Code.objects.update_or_create(defaults={'code': code}, tel=ser.validated_data['tel'])
                return Response({
                    'msg': res['msg'],
                    'code': 1001
                })
        return Response(ser.errors)


class SignUp(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializers

    def create(self, request, *args, **kwargs):
        ser = SignUpSerializers(data=request.data)
        if ser.is_valid():
            user = ser.save()
            key = uuid.uuid4()
            Token.objects.create(key=key, user=user)
            return Response(key)
        return Response(ser.errors)


class SignIn(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignInSerializers

    def create(self, request, *args, **kwargs):
        ser = SignInSerializers(data=request.data)
        if ser.is_valid():
            return Response(ser.validated_data['key'])
        return Response(ser.errors)


class GoodsShow(ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers
    authentication_classes = (MyToken,)
    permission_classes = (MyPermissions, UserPermissions, IsAdminUser,)

    # 动态设置权限: 某类用户才可以添加、删除商品
    def get_permissions(self):
        if self.action == 'create':
            return [IsAdminUser()]
        if self.action == 'delete':
            return [IsAdminUser()]
        return [AllowAny()]

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = Myfilter

    def list(self, request, *args, **kwargs):
        raise MyError()
