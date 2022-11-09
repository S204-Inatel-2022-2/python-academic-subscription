from django.test import TestCase, Client
from django.urls import reverse
import json
from rest_framework import status
from subject.models import Subject
from subject.serializers import SubjectSerializer

# initialize the APIClient app
client = Client()


class GetAllSubjectsTest(TestCase):
    """ Test module for GET all subjects API """

    def setUp(self):
        self.ac1 = Subject.objects.create(
            subject_id='fd0e26dc-e0d8-4142-b639-da3d6b47df91', subject_name='Atividade Complementar 1',
            subject_slug='ac1', total_hours=60, credits=3
        )
        self.c201 = Subject.objects.create(
            subject_id='6ef69dd4-5fbc-4974-ab98-07f11ab3fe2a', subject_name='Introdução a Engenharia',
            subject_slug='c201', total_hours=20, credits=1
        )
        self.c202 = Subject.objects.create(
            subject_id='32fc6dd6-d8ef-42a3-913b-c732c07a7155', subject_name='Algoritmos e Estruturas de Dados I',
            subject_slug='c202', total_hours=120, credits=6
        )
        self.e201 = Subject.objects.create(
            subject_id='61f8d3dc-edd6-4013-9b27-f14389898407', subject_name='Circuitos Elétricos I',
            subject_slug='e201', total_hours=60, credits=3
        )

    def test_get_all_subjects(self):
        # get API response
        response = client.get(reverse('public-subject-list'))
        # get data from db
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleSubjectTest(TestCase):
    """ Test module for GET single subject API """

    def setUp(self):
        self.ac1 = Subject.objects.create(
            subject_id='fd0e26dc-e0d8-4142-b639-da3d6b47df91', subject_name='Atividade Complementar 1',
            subject_slug='ac1', total_hours=60, credits=3
        )
        self.c201 = Subject.objects.create(
            subject_id='6ef69dd4-5fbc-4974-ab98-07f11ab3fe2a', subject_name='Introdução a Engenharia',
            subject_slug='c201', total_hours=20, credits=1
        )
        self.c202 = Subject.objects.create(
            subject_id='32fc6dd6-d8ef-42a3-913b-c732c07a7155', subject_name='Algoritmos e Estruturas de Dados I',
            subject_slug='c202', total_hours=120, credits=6
        )
        self.e201 = Subject.objects.create(
            subject_id='61f8d3dc-edd6-4013-9b27-f14389898407', subject_name='Circuitos Elétricos I',
            subject_slug='e201', total_hours=60, credits=3
        )

    def test_get_valid_single_subject(self):
        response = client.get(
            reverse('public-subject-detail', kwargs={'subject_id': self.ac1.subject_id}))
        subject = Subject.objects.get(subject_id=self.ac1.subject_id)
        serializer = SubjectSerializer(subject)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_subject(self):
        response = client.get(
            reverse('public-subject-detail', kwargs={'subject_id': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewSubjectTest(TestCase):
    """ Test module for inserting a new subject """

    def setUp(self):
        self.valid_payload = {
            'subject_id': 'fd0e26dc-e0d8-4142-b639-da3d6b47df91',
            'subject_name': 'Atividade Complementar 1',
            'subject_slug': 'ac1',
            'total_hours': 60,
            'credits': 3
        }

    def test_not_allow_to_create_subject(self):
        response = client.post(
            reverse('public-subject-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class UpdateSingleSubjectTest(TestCase):
    """ Test module for updating an existing subject """

    def setUp(self):
        self.ac1 = Subject.objects.create(
            subject_id='fd0e26dc-e0d8-4142-b639-da3d6b47df91', subject_name='Atividade Complementar 1',
            subject_slug='ac1', total_hours=60, credits=3
        )
        self.valid_payload = {
            'subject_id': 'fd0e26dc-e0d8-4142-b639-da3d6b47df91',
            'subject_name': 'Atividade Complementar 1',
            'subject_slug': 'ac1',
            'total_hours': 80,
            'credits': 4
        }

    def test_not_allow_to_total_update_subject(self):
        response = client.put(
            reverse('public-subject-detail', kwargs={'subject_id': self.ac1.subject_id}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_not_allow_to_parcial_update_subject(self):
        response = client.patch(
            reverse('public-subject-detail', kwargs={'subject_id': self.ac1.subject_id}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class DeleteSingleSubjectTest(TestCase):
    """ Test module for deleting an existing subject """

    def setUp(self):
        self.ac1 = Subject.objects.create(
            subject_id='fd0e26dc-e0d8-4142-b639-da3d6b47df91', subject_name='Atividade Complementar 1',
            subject_slug='ac1', total_hours=60, credits=3
        )

    def test_not_allow_to_delete_subject(self):
        response = client.delete(reverse('public-subject-detail', kwargs={'subject_id': self.ac1.subject_id}))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
