import traceback

from functools import wraps

from django.conf import settings
from rest_framework import status

from api.common import APIResponse

def response_handler(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            api_response = func(request, *args, **kwargs)
        except Exception as e:
            api_response = APIResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message="Somethig went wrong" if settings.ENV != "development" else str(e),
                traceback=traceback.format_exc()
            )

        return api_response.response()

    return wrapper
