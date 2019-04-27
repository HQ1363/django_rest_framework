import uuid
from yunpian import YunPian

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle

from .serializers import CodeSerializers, RegisterSerializers, LoginSerializers, GuojiSerialzers
from .models import Code, Token, Guoji
from .errors import MyError


class CodeShow(ModelViewSet):
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


class Register(ModelViewSet):
    serializer_class = RegisterSerializers

    def create(self, request, *args, **kwargs):
        ser = RegisterSerializers(data=request.data)
        if ser.is_valid():
            user = ser.save()
            key = uuid.uuid4()
            Token.objects.create(key=key, user=user)
            return Response(key)
        return Response(ser.errors)


class Login(ModelViewSet):
    serializer_class = LoginSerializers

    def create(self, request, *args, **kwargs):
        ser = LoginSerializers(data=request.data)
        if ser.is_valid():
            return Response(ser.validated_data['key'])
        return Response(ser.errors)


class GuojiShow(ModelViewSet):
    queryset = Guoji.objects.all()
    serializer_class = GuojiSerialzers
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('name',)
    search_fields = ('name',)
    ordering_fields = ('xianjia', 'yuanjia')
    ordering = ('id',)
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)

    # 测试自定义异常，手动抛出异常
    def retrieve(self, request, *args, **kwargs):
        raise MyError()
