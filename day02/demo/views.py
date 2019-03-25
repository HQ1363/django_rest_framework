from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Class, Student
from .serializers import ClsSerializers, StuSerializers


class StudentList(APIView):
    def get(self, request):
        stus = Student.objects.all()
        # 多个数据的化需要加上many=True
        ser = StuSerializers(instance=stus, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = StuSerializers(data=request.data)
        if ser.is_valid():
            # 创建新数据
            ser.save()
            # 将新创建的数据返回给前端
            return Response(ser.validated_data)
        # 返回错误信息
        return Response({'msg': ser.errors, 'code': Response.status_code})


# 获取单个，需要参数
class StudentSingle(APIView):
    def get(self, request, id):
        stu = Student.objects.get(id=id)
        ser = StuSerializers(instance=stu)
        return Response(ser.data)

    def put(self, request, id):
        stu = Student.objects.get(id=id)
        ser = StuSerializers(instance=stu, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response({'msg': ser.errors, 'code': Response.status_code})

    def patch(self, request, id):
        stu = Student.objects.get(id=id)
        ser = StuSerializers(instance=stu, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response({'msg': ser.errors, 'code': Response.status_code})

    def delete(self, request, id):
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response(Response.status_code)
