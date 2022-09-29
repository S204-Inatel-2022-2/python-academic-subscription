from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        lookup_field = 'course_id'
        fields = '__all__'
        extra_kwargs = {
            'url': {'lookup_field': 'course_id'}
        }