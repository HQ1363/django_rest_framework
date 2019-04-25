from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler


# 自定义异常类
class MyError(APIException):
    status_code = 456
    default_detail = '出bug了'
    default_code = 'mybug'


# 自定义异常处理函数
def my_handle_error(exc, context):
    response = exception_handler(exc, context)
    # print('============',response.data)

    return response
