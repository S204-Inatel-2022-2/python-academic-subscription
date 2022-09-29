from rest_framework import viewsets
from course.models import Course
from course import serializers


class PublicCourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    lookup_field = 'course_id'
