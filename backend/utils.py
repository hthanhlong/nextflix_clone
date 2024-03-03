from rest_framework.response import Response
from rest_framework import status

class ResponseSuccess(Response):
    def __init__(self, error_code=1, message="", data=None, status=status.HTTP_200_OK, template_name=None, headers=None, exception=False, content_type=None):
        data = {
            "is_success": True,
            "error_code": error_code,
            "message": message,
            "data": data
        }
        super().__init__(data=data, status=status, template_name=template_name, headers=headers, exception=exception, content_type=content_type)



class ResponseBadRequest(Response):
    def __init__(self, error_code=0, message="", data=None, status=status.HTTP_400_BAD_REQUEST, template_name=None, headers=None, exception=False, content_type=None):
        data = {
            "is_success": False,
            "error_code": error_code,
            "message": message,
            "data": data
        }
        super().__init__(data=data, status=status, template_name=template_name, headers=headers, exception=exception, content_type=content_type)