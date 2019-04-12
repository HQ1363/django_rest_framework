from rest_framework.viewsets import ModelViewSet

from .serializers import CountrySerializers, WinePageSerializers, WineInfoSerializers
from .models import Country, WinePage, WineInfo


class CountryShow(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers


class WinePageShow(ModelViewSet):
    queryset = WinePage.objects.all()
    serializer_class = WinePageSerializers


class WineInfoShow(ModelViewSet):
    queryset = WineInfo.objects.all()
    serializer_class = WineInfoSerializers
