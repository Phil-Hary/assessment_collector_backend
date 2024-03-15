from django.db import models

from .base_model import BaseModel

class Form(BaseModel):
    name = models.CharField(max_length=500)
    slug = models.CharField(max_length=500, unique=True)
    config = models.JSONField()

    class Meta:
        db_table = "forms"
