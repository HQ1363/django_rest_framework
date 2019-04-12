# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework import serializers

from .models import Country, WinePage, WineInfo


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class WinePageSerializers(serializers.ModelSerializer):
    class Meta:
        model = WinePage
        fields = '__all__'


class WineInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = WineInfo
        fields = '__all__'
