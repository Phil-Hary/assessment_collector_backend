from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

from api.common import APIResponse
from api.decorators.response_handler import response_handler
from api.models import Form
from api.serializers import FormConfigPayloadSerializer

class FormDetailViewSet(ViewSet):
    @action(detail=False, methods=['GET'], url_path="config")
    @response_handler
    def get_config(self, request, form_name):
        form = None

        try:
            form = Form.objects.get(slug=form_name)
        except Form.DoesNotExist:
            return APIResponse(message="Form does not exists", status_code=status.HTTP_400_BAD_REQUEST)

        return APIResponse(data=form.config, status_code=status.HTTP_200_OK)


    @action(detail=False, methods=['post'], url_path="save_config")
    @response_handler
    def update_config(self, request, form_name):
        form = None

        serialized_payload = FormConfigPayloadSerializer(data=request.data)

        if not serialized_payload.is_valid():
            return APIResponse(message=f"Invalid response {serialized_payload.errors}", status_code=status.HTTP_400_BAD_REQUEST)

        response = serialized_payload.data

        try:
            form = Form.objects.get(slug=form_name)
            form.config = response
            form.save()
        except Form.DoesNotExist:
            return APIResponse(message="Form does not exists", status_code=status.HTTP_400_BAD_REQUEST)

        return APIResponse(message="Form config updated successfully", status_code=status.HTTP_200_OK)