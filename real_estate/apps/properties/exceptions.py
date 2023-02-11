from rest_framework.exceptions import APIException


class PropertyNotFound(APIException):
    status_code = 404
    default_detail = "The requested property does not exist"


class NewProjectNotFound(APIException):
    status_code = 404
    default_detail = "The requested project does not exist"
