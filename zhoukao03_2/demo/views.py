from rest_framework.viewsets import ModelViewSet

from .serializers import GtypeSerializers, GoodsSerializers
from .models import Gtype, Goods


# 3.给接口添加增删改查功能
class GtypeShow(ModelViewSet):
    queryset = Gtype.objects.all()
    serializer_class = GtypeSerializers


# 3.给接口添加增删改查功能
class GoodsShow(ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers
