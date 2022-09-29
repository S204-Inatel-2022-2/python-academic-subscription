from django.test import TestCase, Client
from django.urls import reverse
import json
from rest_framework import status
from course.models import Course
from course.serializers import CourseSerializer

# initialize the APIClient app
client = Client()


class GetAllCoursesTest(TestCase):
    """ Test module for GET all courses API """

    def setUp(self):
        self.ges = Course.objects.create(
            course_id='afded52a-c26c-4e82-8bcd-d906df2e7263', course_name='Engenharia de Software', course_slug='ges',
            period=10, start='2019-01-01', coordinator='Guilherme Baruque', max_students_per_period=50,
            accept_new_inscriptions=True
        )
        self.gec = Course.objects.create(
            course_id='c0c3c77b-b259-4ee1-9098-45a42a0bc4f8', course_name='Engenharia de Computação', course_slug='gec',
            period=10, start='2010-01-01', coordinator='Guilherme Baruque', max_students_per_period=50,
            accept_new_inscriptions=True
        )
        self.gep = Course.objects.create(
            course_id='c03b3a25-d8e3-483d-99e3-1beaa7d85dc5', course_name='Engenharia de Produção', course_slug='gep',
            period=10, start='2015-01-01', coordinator='Breno Tavares', max_students_per_period=50,
            accept_new_inscriptions=True
        )
        self.gee = Course.objects.create(
            course_id='303c37a6-cd1f-4745-ae7f-b2fa50fb986e', course_name='Engenharia Elétrica', course_slug='gee',
            period=10, start='1990-01-01', coordinator='Alexandre Baratella', max_students_per_period=40,
            accept_new_inscriptions=False
        )

    def test_get_all_courses(self):
        # get API response
        response = client.get(reverse('public-course-list'))
        # get data from db
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleCourseTest(TestCase):
    """ Test module for GET single course API """

    def setUp(self):
        self.ges = Course.objects.create(
            course_id='afded52a-c26c-4e82-8bcd-d906df2e7263', course_name='Engenharia de Software', course_slug='ges',
            period=10, start='2019-01-01', coordinator='Guilherme Baruque', max_students_per_period=50,
            accept_new_inscriptions=True
        )
        self.gec = Course.objects.create(
            course_id='c0c3c77b-b259-4ee1-9098-45a42a0bc4f8', course_name='Engenharia de Computação', course_slug='gec',
            period=10, start='2010-01-01', coordinator='Guilherme Baruque', max_students_per_period=50,
            accept_new_inscriptions=True
        )
        self.gep = Course.objects.create(
            course_id='c03b3a25-d8e3-483d-99e3-1beaa7d85dc5', course_name='Engenharia de Produção', course_slug='gep',
            period=10, start='2015-01-01', coordinator='Breno Tavares', max_students_per_period=50,
            accept_new_inscriptions=True
        )
        self.gee = Course.objects.create(
            course_id='303c37a6-cd1f-4745-ae7f-b2fa50fb986e', course_name='Engenharia Elétrica', course_slug='gee',
            period=10, start='1990-01-01', coordinator='Alexandre Baratella', max_students_per_period=40,
            accept_new_inscriptions=False
        )

    def test_get_valid_single_course(self):
        response = client.get(
            reverse('public-course-detail', kwargs={'course_id': self.ges.course_id}))
        course = Course.objects.get(course_id=self.ges.course_id)
        serializer = CourseSerializer(course)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_course(self):
        response = client.get(
            reverse('public-course-detail', kwargs={'course_id': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewCourseTest(TestCase):
    """ Test module for inserting a new course """

    def setUp(self):
        self.valid_payload = {
            'course_id': 'afded52a-c26c-4e82-8bcd-d906df2e7263',
            'course_name': 'Engenharia de Software',
            'course_slug': 'ges',
            'period': 10,
            'start': '2019-01-01',
            'coordinator': 'Guilherme Baruque',
            'max_students_per_period': 50,
            'accept_new_inscriptions': True
        }

    def test_not_allow_to_create_course(self):
        response = client.post(
            reverse('public-course-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class UpdateSingleCourseTest(TestCase):
    """ Test module for updating an existing course """

    def setUp(self):
        self.ges = Course.objects.create(
            course_id='afded52a-c26c-4e82-8bcd-d906df2e7263', course_name='Engenharia de Software', course_slug='ges',
            period=10, start='2019-01-01', coordinator='Guilherme Baruque', max_students_per_period=50,
            accept_new_inscriptions=True
        )
        self.valid_payload = {
            'course_id': 'afded52a-c26c-4e82-8bcd-d906df2e7263',
            'course_name': 'Engenharia de Software',
            'course_slug': 'ges',
            'period': 10,
            'start': '2019-01-01',
            'coordinator': 'Guilherme Baruque',
            'max_students_per_period': 50,
            'accept_new_inscriptions': False
        }

    def test_not_allow_to_total_update_course(self):
        response = client.put(
            reverse('public-course-detail', kwargs={'course_id': self.ges.course_id}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_not_allow_to_parcial_update_course(self):
        response = client.patch(
            reverse('public-course-detail', kwargs={'course_id': self.ges.course_id}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class DeleteSingleCourseTest(TestCase):
    """ Test module for deleting an existing course """

    def setUp(self):
        self.ges = Course.objects.create(
            course_id='afded52a-c26c-4e82-8bcd-d906df2e7263', course_name='Engenharia de Software', course_slug='ges',
            period=10, start='2019-01-01', coordinator='Guilherme Baruque', max_students_per_period=50,
            accept_new_inscriptions=True
        )

    def test_not_allow_to_delete_course(self):
        response = client.delete(reverse('public-course-detail', kwargs={'course_id': self.ges.course_id}))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
