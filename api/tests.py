from django.utils.six import BytesIO
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.test import APIClient
from rest_framework_jwt.compat import get_user_model
from django.test import TestCase

User = get_user_model()


class AuthTest(TestCase):
    """JSON Web Token Authentication"""

    def setUp(self):
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.username = 'test_user'
        self.email = 'test_user@csumb.edu'
        self.password = 'test_user_password'
        self.user = User.objects.create_user(self.username, self.email, self.password)

    def test_passing_auth(self):
        """
        Hitting the authentication backend with correct password.
        Ensure the a token is returned as response
        """
        response = self.csrf_client.post(
            '/auth/token/',
            {
                'username': self.username,
                'password': self.password
            })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = JSONParser().parse(BytesIO(response.content))
        self.assertTrue('token' in data)

    def test_failing_auth(self):
        """
            Hitting the authentication backend with incorrect password.
            Observe 400 BAD request
        """
        response = self.csrf_client.post(
            '/auth/token/',
            {
                'username': self.username,
                'password': self.password + '123'
            })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
