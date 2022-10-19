from django.db import models
from uuid import uuid4


class Course(models.Model):
    objects = models.Manager()
    course_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    course_name = models.CharField(max_length=50)
    course_slug = models.CharField(max_length=50)
    period = models.IntegerField()
    start = models.DateField()
    coordinator = models.CharField(max_length=50)
    max_students_per_period = models.IntegerField()
    accept_new_inscriptions = models.BooleanField()

