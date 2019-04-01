from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from django_filters.rest_framework.backends import DjangoFilterBackend
from django_filters.rest_framework.filters import OrderingFilter
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
import uuid
from .models import Book, User
from .serializers import BookSerializers, RegisterSerializers, LoginSerializers


class Bearer(TokenAuthentication):
    keyword = 'Bearer'


class Booklist(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ['name', 'price']
    search_fields = ('=name', 'price', 'author')
    ordering_fields = ('price', 'name', 'author')
    ordering = ('name',)

    # 单个视图配置认证类，配置多个认证类，通过其中一个认证，就可以
    # authentication_classes = (TokenAuthentication, Bearer)
    authentication_classes = (BasicAuthentication,)
    # 权限设置，只有认证通过的用户才有权限
    permission_classes = (IsAuthenticated,)


class Register(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers

    def get(self, request):
        return Response('hello')

    def post(self, request):
        # 获取前端post过来的数据反序列化
        ser = RegisterSerializers(data=request.data)
        if ser.is_valid():
            # user获取用户对象
            user = ser.save()
            # 对Token表的key进行hash加密
            key = uuid.uuid4()
            # 为用户生成token，key值可不传，有默认方法获取，可参考Token中代码
            Token.objects.create(user=user, key=key)
            return Response(ser.validated_data)
        return Response(ser.errors, Response.status_code)


class Login(APIView):
    def post(self, request):
        ser = LoginSerializers(data=request.data)
        if ser.is_valid():
            token = ser.validated_data['token']
            return Response('token')
        return Response(ser.errors, Response.status_code)
