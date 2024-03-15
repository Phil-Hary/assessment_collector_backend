from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import FormResponse

from .base_model import BaseModel

class FormResponseType(models.TextChoices):
    STRING = 'STRING', _('STRING')
    BOOL = 'BOOL', _('BOOL')
    INT = 'INT', _('INT')
    DATE = 'DATE', _('DATE')

class ResponseValue(BaseModel):
    field_name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=FormResponseType.choices)
    value = models.CharField(max_length=500, blank=True)
    form_response = models.ForeignKey(FormResponse, on_delete=models.CASCADE, related_name="response_values")

    class Meta:
        db_table = "response_values"