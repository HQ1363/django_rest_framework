import uuid

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import LoginSerializers, DashaSerializers, CompanySerializers
from .models import Dasha, Company


class Login(ModelViewSet):
    serializer_class = LoginSerializers

    def create(self, request, *args, **kwargs):
        ser = LoginSerializers(data=request.data)
        if ser.is_valid():
            return Response(ser.validated_data['key'])
        return Response(ser.errors)


class DashaShow(ModelViewSet):
    queryset = Dasha.objects.all()
    serializer_class = DashaSerializers


class CompanyShow(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
