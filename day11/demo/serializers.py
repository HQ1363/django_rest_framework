# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework import serializers

from .models import User, Student


class StudentSerializers(serializers.ModelSerializer):
    age = serializers.IntegerField(max_value=99, min_value=1)

    class Meta:
        model = Student
        fields = '__all__'
