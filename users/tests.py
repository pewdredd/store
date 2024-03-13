from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.models import User


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse('users:registration')
        self.data = {'first_name': 'Amir', 'last_name': 'Ak',
                     'username': 'pewdredd', 'email': 'pew@gmail.com',
                     'password1': 'qwerty777&', 'password2': 'qwerty777&'
                     }

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertEquals(response.context_data['title'], 'Store - Registration')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_post_success(self):
        self.assertFalse(User.objects.filter(username=self.data['username']).exists())

        # Checkin registration form
        response = self.client.post(self.path, self.data)
        self.assertEquals(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, 'users:login')
        self.assertTrue(User.objects.filter(username=self.data['username']).exists())

    def test_user_registration_post_error(self):
        User.objects.create(username=self.data['username'])
        response = self.client.post(self.path, self.data)
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)



