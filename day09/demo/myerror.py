# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
from rest_framework import status


class MyError(APIException):
    default_detail = 'BUG'
    default_code = '444'


# 自定义异常处理函数
def my_handle_error(exc, context):
    response = exception_handler(exc, context)
    return response
