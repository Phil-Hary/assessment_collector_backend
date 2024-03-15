from rest_framework import serializers

from api.models import Form
from .form_detail import FormConfigPayloadSerializer

class FormModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ["name", "slug"]

class CreateFormPayloadSerialzier(serializers.Serializer):
    name = serializers.CharField(max_length=500)
    slug = serializers.CharField(max_length=500)
    config = FormConfigPayloadSerializer()