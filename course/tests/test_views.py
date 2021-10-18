from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from course_api.models import Course, Category, Contact, Branch
from django.test import Client

client = Client()

class TestCourse(APITestCase):
    url = reverse('coursesList')

    def test_create_course_object(self):

        data = {
            "name": "баскетбол",
            "description": "бла-бла-бла",
            "contact": [
                {
                    "type": 1,
                    "value": 9967029988
                }
            ],
            "branch": [
                {
                    "latitude": 45843473,
                    "longitude": 48474733,
                    "address": "улица Колотушкина"
                }
            ],
            "category": {
                "name": "спорт",
                "img_path": "jpg"
            },
            "logo": "мяч"
        }

        response = self.client.post(self.url, data, format='json')
        result=response.json()
        self.assertEqual(response.status_code, 200)

    def test_get_list_of_courses(self):

        response = self.client.get(self.url)
        result=response.json()
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        contacts = []
        branches = []
        test_category = Category.objects.create(name='творчество', imgpath = "jpg")
        test_branch = Branch.objects.create(latitude = 466654332, longitude = 3434566, address = "Бейкер стрит")
        test_contact = Contact.objects.create(type = 1, value = 474547473)
        contacts.append(test_contact)
        branches.append(test_branch)
        test_course = Course.objects.create(
            name='гончарный',
            description='бла-бла-бла',
            logo='ваза',
            category = test_category,
        )
        self.course.contacts.add(*contacts)
        self.course.branches.add(*branches)

    def test_detail_view_get(self):
        url = reverse('courseDetail', kwargs={'pk': self.course.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_delete(self):
        url = reverse('courseDetail', kwargs={'pk': self.course.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_detail_update(self):
        url = reverse('courseDetail', kwargs={'pk': self.course.pk})
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
