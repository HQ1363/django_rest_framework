from yunpian import YunPian

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import CodeSerializers
from .models import Code


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
