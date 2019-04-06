import yunpian

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import *
from .models import *


class TelcodeShow(ModelViewSet):
    serializer_class = TelcodeSerializers

    def create(self, request, *args, **kwargs):
        ser = TelcodeSerializers(data=request.data)
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
                Telcode.objects.update_or_create(defaults={'code': code}, tel=ser.validated_data['tel'])
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
            token = Token.objects.create(key=key, user=user)
            return Response(token.key)
        return Response(ser.errors)


class Login(ModelViewSet):
    serializer_class = LoginSerializers

    def create(self, request, *args, **kwargs):
        ser = LoginSerializers(data=request.data)
        if ser.is_valid():
            return Response(ser.validated_data['key'])
        return Response(ser.errors)


class UserShow(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class OrderShow(ModelViewSet):
    queryset = Order.objects.all()
    serializers = OrderSerializers


class GoodstypeShow(ModelViewSet):
    queryset = GoodsType.objects.all()
    serializers = GoodstypeSerializers


class GoodsShow(ModelViewSet):
    queryset = Goods.objects.all()
    serializers = GoodsSerializers
