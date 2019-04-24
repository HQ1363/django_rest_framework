import uuid

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import SigninSerializers, SignupSerializers
from .models import User, Token


class SignUp(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignupSerializers

    def create(self, request, *args, **kwargs):
        ser = SignupSerializers(data=request.data)
        if ser.is_valid():
            user = ser.save()
            key = uuid.uuid4()
            Token.objects.create(key=key, user=user)
            return Response(key)
        return Response(ser.errors)


class SignIn(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SigninSerializers

    def create(self, request, *args, **kwargs):
        ser = SigninSerializers(data=request.data)
        if ser.is_valid():
            return Response(ser.validated_data['key'])
        return Response(ser.errors)
