from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import Registerserializers, Loginserializers


class Register(APIView):
    def post(self, request):
        ser = Registerserializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response(ser.errors, Response.status_code)


class Login(APIView):
    def post(self, request):
        ser = Loginserializers(data=request.data)
        if ser.is_valid():
            return Response(ser.validated_data)
        return Response(ser.errors, Response.status_code)
