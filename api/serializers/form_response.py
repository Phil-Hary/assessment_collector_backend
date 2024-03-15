from rest_framework import serializers

from api.models import FormResponseType

class ResponseSerializer(serializers.Serializer):
    field_name = serializers.CharField(max_length=500)
    value = serializers.CharField(max_length=500, allow_blank=True)
    type = serializers.ChoiceField(choices=FormResponseType.choices)

class FormResponsePayloadSerializer(serializers.Serializer):
    response = ResponseSerializer(many=True)
