import uuid

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import CodeSerializers
from .models import Code, User, Token


class CodeShow(ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializers

    def create(self, request, *args, **kwargs):
        ser = CodeSerializers(data=request.data)
        if ser.is_valid():
            yun = yunpian.Yunpian()
            code = yun.makecode()
