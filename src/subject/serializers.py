from rest_framework import serializers
from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        lookup_field = 'subject_id'
        fields = '__all__'
        extra_kwargs = {
            'url': {'lookup_field': 'subject_id'}
        }
