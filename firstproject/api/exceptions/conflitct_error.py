from http import HTTPStatus
from rest_framework.exceptions import APIException, _get_error_details

class ConflictError(APIException):
    status_code = HTTPStatus.CONFLICT
    default_detail = 'Conflict error'
    default_code = 'conflict_error'