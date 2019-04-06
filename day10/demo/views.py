import uuid

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import RegisterSerializers, LoginSerializers, UserSerializers, CommentSerializers
from .models import User, Token, Comment
from .myauthentication import TokenAuth
from .mypermission import MyPermissions
from .mythrottle import NoAuth, YesAuth


class Register(APIView):
    def post(self, request):
        ser = RegisterSerializers(data=request.data)
        if ser.is_valid():
            user = ser.save()
            token = uuid.uuid4()
            Token.objects.create(key=token, user=user)
            return Response(token)
        return Response(ser.errors, Response.status_code)


class Login(APIView):
    def post(self, request):
        ser = LoginSerializers(data=request.data)
        if ser.is_valid():
            return Response(ser.validated_data['token'])
        return Response(ser.errors, Response.status_code)


class CommentShow(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    authentication_classes = (TokenAuth,)
    permission_classes = (MyPermissions,)
    throttle_classes = (NoAuth, YesAuth)
