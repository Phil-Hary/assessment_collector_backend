from rest_framework import serializers
from django.db import models
from django.utils.translation import gettext_lazy as _

class TemplateType(models.TextChoices):
    FORM = 'form', _('form')

class LayoutType(models.TextChoices):
    SIMPLE = 'simple', _('simple')

class ComponentType(models.TextChoices):
    TEXT_FIELD = 'text-field', _('text-field')
    DROPDOWN = 'dropdown', _('dropdown')
    NUMBER_FIELD = 'number-field', _('number-field')
    DATE_FIELD = 'date-field', _('date-field')
    TEXT_AREA = 'text-area', _('text-area')

class RequestMethod(models.TextChoices):
    POST = 'post', _('post')

class OptionSerializer(serializers.Serializer):
    label = serializers.CharField(max_length=500)
    value = serializers.CharField(max_length=500)

class FormFieldSerializer(serializers.Serializer):
    label = serializers.CharField(max_length=500)
    componentType = serializers.ChoiceField(choices=ComponentType.choices)
    fieldName = serializers.CharField(max_length=500)
    placeholder = serializers.CharField(max_length=500, required=False)
    required = serializers.BooleanField()
    options = OptionSerializer(many=True, required=False)

    def validate(self, data):
        if data['componentType'] == ComponentType.DROPDOWN:
            if not data.get("options"):
                raise serializers.ValidationError("options in required for dropdown components")
        else:
            if not data.get("placeholder") and data['componentType'] != ComponentType.DATE_FIELD:
                raise serializers.ValidationError("valid placeholder in required for non-dropdown components")
        
        return data

class onCancelSerilaizer(serializers.Serializer):
    label = serializers.CharField(max_length=500)
    navigateTo = serializers.CharField(max_length=500)

class OnActionSerializer(serializers.Serializer):
    reset = serializers.BooleanField()
    toast = serializers.CharField(max_length=500)
    navigateTo = serializers.CharField(max_length=500, allow_blank=True)

class ApiConfigSerializer(serializers.Serializer):
    endpoint = serializers.CharField(max_length=500)
    requestMethods = serializers.ChoiceField(choices=RequestMethod.choices)
    onSuccess = OnActionSerializer()
    onError = OnActionSerializer()

class OnSubmissionSerializer(serializers.Serializer):
    label = serializers.CharField(max_length=500)
    apiConfig = ApiConfigSerializer()

class ContentSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=500)
    subTitle = serializers.CharField(max_length=500)
    layout = serializers.ChoiceField(choices=LayoutType.choices)
    formFields = FormFieldSerializer(many=True)
    onSubmission = OnSubmissionSerializer()
    onCancel = onCancelSerilaizer()


class PageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=500)
    template = serializers.ChoiceField(choices=TemplateType.choices)
    content = ContentSerializer()

class FormConfigPayloadSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=500)
    pages = PageSerializer(many=True)
