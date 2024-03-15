from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

from api.common import APIResponse
from api.decorators.response_handler import response_handler
from api.models import Form
from api.serializers import FormConfigPayloadSerializer

class FormDetailViewSet(ViewSet):
    """
        This class contains the form detail related views.
        Holds the logic to get and update a form's config
    """
    @action(detail=False, methods=['GET', "POST"], url_path="config")
    @response_handler
    def get_config(self, request, form_name):
        form = None

        try:
            form = Form.objects.get(slug=form_name)
        except Form.DoesNotExist:
            return APIResponse(message="Form does not exists", status_code=status.HTTP_404_NOT_FOUND)
        
        if request.method == "GET":
            return APIResponse(data=form.config, status_code=status.HTTP_200_OK)
        
        elif request.method == "POST":
            serialized_payload = FormConfigPayloadSerializer(data=request.data)

            if not serialized_payload.is_valid():
                return APIResponse(message=f"Invalid config {serialized_payload.errors}", status_code=status.HTTP_400_BAD_REQUEST)

            response = serialized_payload.data

            try:
                form.config = response
                form.save()
            except Exception:
                return APIResponse(message="An error occurred while saving the config", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return APIResponse(message="Form config updated successfully", status_code=status.HTTP_200_OK)


        