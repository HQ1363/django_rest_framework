from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserInfo
from .serializers import UserSerializers, UserModelSerializers


class Userlist(APIView):
    def get(self, request):
        users = UserInfo.objects.all()
        ser = UserSerializers(instance=users, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = UserSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response(ser.errors, Response.status_code)


class Usersingle(APIView):
    def get(self, request, pk):
        user = UserInfo.objects.get(id=pk)
        ser = UserSerializers(instance=user)
        return Response(ser.data)

    def put(self, request, pk):
        user = UserInfo.objects.get(id=pk)
        ser = UserSerializers(instance=user, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response(ser.errors, Response.status_code)

    def delete(self, request, pk):
        user = UserInfo.objects.get(id=pk)
        user.delete()
        return Response(Response.status_code)
