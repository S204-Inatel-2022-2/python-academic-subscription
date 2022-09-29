from rest_framework import viewsets
from subject.models import Subject
from subject import serializers


class PublicSubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
