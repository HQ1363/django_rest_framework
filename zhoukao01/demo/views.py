from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClaSerializers, StuSerializers
from .models import StuClass, Student


# 班级列表接口
class Stuclasslist(APIView):
    def get(self, request):
        cls = StuClass.objects.all()
        ser = ClaSerializers(instance=cls, many=True)
        return Response(ser.data)

    # 创建班级的API接口
    def post(self, request):
        ser = ClaSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response(ser.errors, Response.status_code)


# 班级详情接口
class StuclassSingle(APIView):
    def get(self, request, id):
        cls = StuClass.objects.get(id=id)
        ser = ClaSerializers(instance=cls)
        return Response(ser.data)

    # 修改班级信息接口
    def put(self, request, id):
        cls = StuClass.objects.get(id=id)
        ser = ClaSerializers(instance=cls, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response(ser.errors, Response.status_code)

    # 删除班级信息接口
    def delete(self, request, id):
        cls = StuClass.objects.get(id=id)
        cls.delete()
        return Response(Response.status_code)


# 学生列表接口
class Studentlist(APIView):
    def get(self, request):
        stus = Student.objects.all()
        ser = StuSerializers(instance=stus, many=True)
        return Response(ser.data)

    # 创建学生信息接口
    def post(self, request):
        ser = StuSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response(ser.errors, Response.status_code)


# 学生详情接口
class StudentSingle(APIView):
    def get(self, request, id):
        stu = Student.objects.get(id=id)
        ser = StuSerializers(instance=stu)
        return Response(ser.data)

    # 修改学生信息接口
    def put(self, request, id):
        stu = Student.objects.get(id=id)
        ser = StuSerializers(instance=stu, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        return Response(ser.errors, Response.status_code)

    # 删除学生信息接口
    def delete(self, request, id):
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response(Response.status_code)
