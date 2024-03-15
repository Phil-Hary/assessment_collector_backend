from django.db import IntegrityError
from rest_framework import status
from rest_framework.views import APIView

from api.models import Form
from api.serializers import FormModelSerializer, CreateFormPayloadSerialzier
from api.common import APIResponse
from api.decorators.response_handler import response_handler


class FormApiView(APIView):
    @response_handler
    def get(self, request):
        """
            This view returns all the forms present in the db
        """
        forms = Form.objects.all()
        serialized_form = FormModelSerializer(forms, many=True)

        return APIResponse(
            data=serialized_form.data
        )

    @response_handler
    def post(self, request):
        """
            This view helps to create a new form, by validating the config
        """
        form = None

        serialized_payload = CreateFormPayloadSerialzier(data=request.data)

        if not serialized_payload.is_valid():
            return APIResponse(message=f"Invalid payload {serialized_payload.errors}", status_code=status.HTTP_400_BAD_REQUEST)

        payload = serialized_payload.data
                            

        try:
            form = Form.objects.create(
                name=payload.get("name"),
                slug=payload.get("slug"),
                config=payload.get("config")
            )
        except IntegrityError:
            return APIResponse(message="A form with the same slug already exists", status_code=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return APIResponse(message="Error occurred while creating the form", status_code=status.HTTP_400_BAD_REQUEST)

        return APIResponse(message="Form created successfully", status_code=status.HTTP_200_OK)