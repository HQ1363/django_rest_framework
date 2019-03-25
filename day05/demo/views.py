from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import Type, Goods, Order


class Typelist(APIView):
    def get(self, request):
        types = Type.objects.all()
        ser = Typeserializers(instance=types, many=True)
        return Response(ser.data)


class Typesingle(APIView):
    def get(self, request, id):
        type = Type.objects.get(id=id)
        ser = Typeserializers(instance=type)
        return Response(ser.data)


class Goodslist(APIView):
    def get(self, request):
        goods = Goods.objects.all()
        ser = Goodserializers(instance=goods, many=True)
        return Response(ser.data)


class Orderlist(APIView):
    def get(self, request):
        orders = Order.objects.all()
        ser = Orderserializers(instance=orders, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = Orderserializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response(ser.errors, Response.status_code)


class Ordersingle(APIView):
    def get(self, request, id):
        order = Order.objects.get(id=id)
        ser = Orderserializers(instance=order)
        return Response(ser.data)

    def post(self, request, id):
        order = Order.objects.get(id=id)
        ser = Orderserializers(instance=order, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response(ser.errors, Response.status_code)
