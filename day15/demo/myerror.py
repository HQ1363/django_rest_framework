# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler


class MyError(APIException):
    status_code = 444
    default_detail = '出BUG了'
    default_code = '自定义错误'


def my_exception_handler(exc, context):
    response = exception_handler(exc, context)
    return response
