from yunpian import YunPian
import uuid

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import CodeSerializers, SignUpSerializers, SignInSerializers
from .models import Code, User, Token


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
