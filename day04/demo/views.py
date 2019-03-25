from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from .models import Type, Goods
from .serializers import TypeSerializers, Goodserizlizers


class Typelist(mixins.CreateModelMixin, mixins.ListModelMixin, GenericAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Goodslist(mixins.CreateModelMixin, mixins.ListModelMixin, GenericAPIView):
    queryset = Goods.objects.all()
    serializer_class = Goodserizlizers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Goodsingle(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Goods.objects.all()
    serializer_class = Goodserizlizers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
