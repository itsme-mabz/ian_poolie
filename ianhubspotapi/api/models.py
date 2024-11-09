# myapp/models.py
from django.db import models
from jsonfield import JSONField

class GenericData(models.Model):
    data = JSONField()  # Field to store arbitrary JSON data
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data Entry {self.id}"
