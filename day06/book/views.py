from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from .models import Book
from .serializers import Bookserializers


class Booklist(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Booksingle(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
