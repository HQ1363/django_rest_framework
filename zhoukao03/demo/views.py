import yunpian
import uuid

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import User, Token, SmsCaptcha
from .serializers import SmsCaptchaSerializers, RegisterSerializers, LoginSerializers, UserSerializers


class SmsViewSet(ModelViewSet):
    queryset = SmsCaptcha.objects.all()
    serializer_class = SmsCaptchaSerializers

    def create(self, request, *args, **kwargs):
        ser = SmsCaptchaSerializers(data=request.data)
        if ser.is_valid():
            yun = yunpian.YunPian()
            code = yun.make_code()
            res = yun.send_code(ser.validated_data['tel'], code)
            if res['code'] != 0:
                return Response({
                    'msg': res['msg'],
                    'code': 1001
                })
            else:
                SmsCaptcha.objects.update_or_create(defaults={'code': code}, tel=ser.validated_data['tel'])
                return Response({
                    'msg': res['msg'],
                    'code': 1005
                })
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
            return Response(key)
        return Response(ser.errors)


class Login(ModelViewSet):
    serializer_class = LoginSerializers

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        if ser.is_valid():
            return Response(ser.validated_data['key'])
        return Response(ser.errors)


# 9.	完成用户列表接口，用POSTMAN展示出所有用户数据
class UserShow(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
