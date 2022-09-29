from django.db import models
from uuid import uuid4

# Create your models here.
class Subject(models.Model):
    subject_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    subject_name = models.CharField(max_length=50)
    subject_slug = models.CharField(max_length=50)
    total_hours = models.IntegerField()
    credits = models.IntegerField()
