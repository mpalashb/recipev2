"""Test for user api"""
import email
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    """Create a new user"""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        return super().setUp()

    def test_create_user_success(self):
        """Test creating a user is successful"""

        payload = {
            'email': 'test@palash.palash',
            'password': 'TestPass1234'
        }

        res = self.client.post(
            CREATE_USER_URL,
            payload
        )

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        # password must not in response data retrived
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Send back the 400 bad req if user already exists"""
        payload = {
            'email': 'test@palash.palash',
            'password': 'TestPass1234'
        }

        create_user(payload)

        res = self.client.post(
            CREATE_USER_URL,
            payload
        )

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_passwod_too_short(self):
        """Test the error If password going to be too shorter"""

        payload = {
            "email": "test1@palash.palash",
            "password": "a"
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
