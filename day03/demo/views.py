from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Type, Goods
from .modelserializers import Typeserializers, Goodsserializers, TySerializers


class Typelist(APIView):
    def get(self, request):
        types = Type.objects.all()
        ser = Typeserializers(instance=types, many=True)
        return Response(ser.data)

    def post(self, request):
        data = request.data
        ser = Typeserializers(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response(ser.errors, Response.status_code)


class Goodslist(APIView):
    def get(self, request):
        goods = Goods.objects.all()
        ser = Goodsserializers(instance=goods, many=True)
        return Response(ser.data)

    def post(self, request):
        data = request.data
        ser = Goodsserializers(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response(ser.errors, Response.status_code)


class Good(APIView):
    def get(self, request, id):
        goods = Goods.objects.get(id=id)
        ser = Goodsserializers(instance=goods)
        return Response(ser.data)

    def post(self, request, id):
        data = request.data
        goods = Goods.objects.get(id=id)
        ser = Goodsserializers(instance=goods, data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response(ser.errors, Response.status_code)
