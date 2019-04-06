import uuid

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import RegisterSerializers, LoginSerializers, UserSerializers
from .models import User, Token
from .myauthentication import MyAuthentication


class Register(APIView):
    def post(self, request):
        ser = RegisterSerializers(data=request.data)
        if ser.is_valid():
            user = ser.save()
            token = uuid.uuid4()
            Token.objects.create(token=token, user=user)
            return Response(token)
        return Response(ser.errors, Response.status_code)


class Login(APIView):
    def post(self, request):
        ser = LoginSerializers(data=request.data)
        if ser.is_valid():
            return Response(ser.validated_data['token'])
        return Response(ser.errors, Response.status_code)


class UserShow(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    authentication_classes = (MyAuthentication,)
