from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework import status

from api.common import APIResponse
from api.decorators.response_handler import response_handler
from api.models import Form, FormResponse, ResponseValue
from api.serializers import FormResponsePayloadSerializer
from api.utils import tranform_response

class FormResposeViewSet(ViewSet):

    @action(detail=False, methods=['post'], url_path="onSubmit")
    @response_handler
    def on_submit(self, request, form_name):
        form = None

        serialized_payload = FormResponsePayloadSerializer(data=request.data)

        if not serialized_payload.is_valid():
            return APIResponse(message=f"Invalid response {serialized_payload.errors}", status_code=status.HTTP_400_BAD_REQUEST)

        response = serialized_payload.data
        response_values = response.get("response")

        try:
            form = Form.objects.get(slug=form_name)
        except Form.DoesNotExist:
            return APIResponse(message="Form does not exists", status_code=status.HTTP_400_BAD_REQUEST)


        form_response = FormResponse.objects.create(form=form)

        for response_value in response_values:
            ResponseValue.objects.create(
                field_name=response_value.get("field_name"),
                type=response_value.get("type"),
                value=response_value.get("value"),
                form_response=form_response
            )
        
        return APIResponse(message="Form response saved successfully", status_code=status.HTTP_200_OK)

        
    @action(detail=False, methods=['get'], url_path="responses")
    @response_handler
    def get_reponses(self, request, form_name):
        form = None
        responses = []

        try:
            form = Form.objects.get(slug=form_name)
        except Form.DoesNotExist:
            return APIResponse(message="Form does not exists", status_code=status.HTTP_400_BAD_REQUEST)
    
        form_responses = FormResponse.objects.prefetch_related().filter(form=form)

        for form_response in form_responses:
            response = form_response.response_values.all()
            responses.append(tranform_response(response, form_response.id))

        
        return APIResponse(
            data=responses,
            message="Responses fetched successfully",
            status_code=status.HTTP_200_OK
        )
        
