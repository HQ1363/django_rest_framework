# 10.	对以上代码进行注释，并且有调试的过程
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import TypesSerializers, GoodsSerializers
from .models import Types, Goods


# 5.	使用GenericAPIView对数据进行渲染
class TypeShow(ModelViewSet):
    # 7.    对商品完成添加，修改, 删除功能
    # 8.    对分类完成添加，修改, 删除功能
    # 9.    对商品和分类完成查看详情功能
    queryset = Types.objects.all()
    serializer_class = TypesSerializers
    authentication_classes = (BasicAuthentication,)
    # 6.  对接口添加权限，用户未登录不可以进行访问
    permission_classes = (IsAuthenticated,)


class GoodShow(ModelViewSet):
    # 7.    对商品完成添加，修改, 删除功能
    # 8.    对分类完成添加，修改, 删除功能
    # 9.    对商品和分类完成查看详情功能
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers
    authentication_classes = (BasicAuthentication,)
    # 6.  对接口添加权限，用户未登录不可以进行访问
    permission_classes = (IsAuthenticated,)
