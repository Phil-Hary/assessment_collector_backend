from django.db import models

from api.models import Form

from .base_model import BaseModel

class FormResponse(BaseModel):
    form = models.ForeignKey(Form, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "form_responses"