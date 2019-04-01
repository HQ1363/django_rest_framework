import yunpian

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import *
from .myauthentication import MyAuth
from .mypermission import MyPermission
from .mythrottle import MyThrottle
from .mypagination import MyPage
from .myerror import MyError


class TelCode(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = CodeSerializers

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        if ser.is_valid():
            yun = yunpian.YunPian()
            code = yun.make_code()
            res = yun.send_code(ser.validated_data['tel'], code)
            if res['code'] != 0:
                return Response({'message': res['msg'], 'code': 1001})
            else:
                Code.objects.update_or_create(defaults={'code': code}, tel=ser.validated_data['tel'])
                return Response({'message': res['msg'], 'code': 1000})
        return Response(ser.errors)


class Register(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers

    def create(self, request, *args, **kwargs):
        ser = RegisterSerializers(data=request.data)
        if ser.is_valid():
            user = ser.save()
            key = uuid.uuid4()
            Token.objects.create(key=key, user=user)
            return Response('注册成功')
        return Response(ser.errors, Response.status_code)


class Login(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializers

    def create(self, request, *args, **kwargs):
        ser = LoginSerializers(data=request.data)
        if ser.is_valid():
            return Response('登陆成功')
        return Response(ser.errors, Response.status_code)


class GoodsShow(ModelViewSet):
    queryset = Goods
    serializer_class = GoodsSerializers
    # 认证
    authentication_classes = (MyAuth,)
    # 权限
    permission_classes = (MyPermission,)
    # 限速
    throttle_classes = (MyThrottle,)
    # 分页
    pagination_class = MyPage
    # 使排序和过滤生效
    filter_backends = (SearchFilter, OrderingFilter)
    #  搜索字段
    search_fields = ('=name',)
    #  排序字段
    order_fields = ('id',)
    # 默认排序
    ordering = ('-id',)

    # 错误信息
    def retrieve(self, request, *args, **kwarg):
        raise MyError()
