from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StuSerializers


# 前端访问同一个接口（url），根据前端不同的访问方法，执行不同的方法（get,port,put,delete,patch）
# 注意，类名不要和models中类名（表名）重复
class StudentList(APIView):
    # 查询
    def get(self, request):
        stu = Student.objects.all()
        # 将数据对象，序列化为前端需要的数据类型
        stus = StuSerializers(instance=stu, many=True)
        return Response(stus.data)

    # 添加
    def post(self, request):
        # 反序列化，只需要前端发送过来的数据,必须使用参数赋值的形式传参
        stu = StuSerializers(data=request.data)
        # 验证数据合法性
        if stu.is_valid():
            stu.save()
            # validated_data 里面是合法的数据
            return Response(stu.validated_data)
        return Response(Response.status_code)


class StudentSingle(APIView):
    # 查询
    def get(self, request, id):
        stu = Student.objects.get(id=id)
        # 将数据对象，序列化为前端需要的数据类型
        stus = StuSerializers(instance=stu)
        return Response(stus.data)

    # 修改
    def put(self, request, id):
        stu = Student.objects.get(id=id)
        stu_post = StuSerializers(instance=stu, data=request.data)
        if stu_post.is_valid():
            stu_post.save()
            return Response(stu_post.validated_data)
        return Response(stu_post.errors, Response.status_code)

    # 部分修改
    def patch(self, request, id):
        stu = Student.objects.get(id=id)
        stu_patch = StuSerializers(instance=stu, data=request.data)
        if stu_patch.is_valid():
            stu_patch.save()
            return Response(stu_patch.validated_data)
        return Response(Response.status_code)

    # 删除
    def delete(self, request, id):
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response(Response.status_code)
