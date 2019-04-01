import yunpian

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import User, Token, SmsCaptcha
from .serializers import SmsCaptchaSerializers, RegisterSerializers, LoginSerializers, UserSerializers


class Sms(CreateAPIView, GenericAPIView):
    def create(self, request, *args, **kwargs):
        yun = yunpian.YunPian()
        code = yun.make_code()
        res = yun.send_code(request.user.phone, code)
        if res['code'] != 0:
            return Response(res['code'] and res['msg'])
        return Response(res['code'] and res['msg'])


class Register(APIView):
    def post(self, reqest):
        ser = RegisterSerializers(data=reqest.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response(ser.errors, Response.status_code)


class Login(APIView):
    def post(self, reqest):
        ser = LoginSerializers(data=reqest.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response(ser.errors, Response.status_code)


# 9.	完成用户列表接口，用POSTMAN展示出所有用户数据
class UserShow(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    # 7.项目支持basic auth认证
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
