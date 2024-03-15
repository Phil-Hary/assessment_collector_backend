from django.conf import settings
from django.http import JsonResponse
from rest_framework import status

class APIResponse:
    def __init__(self, status_code=status.HTTP_200_OK, message="", data = [], traceback=None):
        self.status_code = status_code
        self.message = message
        self.data = data
        self.status = "SUCCESS" if status_code == status.HTTP_200_OK else "FAILURE"
        self.traceback = traceback

    def response(self):
        response_body = {
            "status": self.status,
            "message": self.message,
            "data": self.data
        }

        if settings.ENV == "development" and  self.traceback:
            response_body["traceback"] = self.traceback
            
        return JsonResponse(response_body, status=self.status_code)