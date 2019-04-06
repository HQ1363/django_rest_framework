import yunpian

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import CodeSerializers, RegisterSerializers
from .models import Code, User


class CodeShow(ModelViewSet):
    serializer_class = CodeSerializers

    def create(self, request, *args, **kwargs):
        ser = CodeSerializers(data=request.data)
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
                Code.objects.update_or_create(defaults={'code': code}, tel=ser.validated_data['tel'])
                return Response({
                    'msg': res['msg'],
                    'code': 1000
                })
        return Response(ser.errors)


class Register(ModelViewSet):
    serializer_class = RegisterSerializers

    def create(self, request, *args, **kwargs):
        ser = RegisterSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response(ser.errors)
