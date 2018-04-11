from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.six import BytesIO
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.test import APIClient

User = get_user_model()

class ChallengeTest(TestCase):
    data: any
    #I have no idea what's going on with this -J
    def setUp(self):
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.username = 'test_user'
        self.email = 'test_user@csumb.edu'
        self.password = 'test_user_password'
        self.user = User.objects.create_user(self.username, self.email, self.password)

        response = self.csrf_client.post(
            '/auth/token/',
            {
                'username': self.username,
                'password': self.password
            })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = JSONParser().parse(BytesIO(response.content))
        self.assertTrue('token' in data)

    def get_challenges(self):
        response = self.csrf_client.post(
            '/challenge/GET',
            {
                'token': self.data['token']
            })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = JSONParser().parse(BytesIO(response.content))
        self.assertTrue('token' in data)




    def post_challenges(self):
        self


    def get_challenge_valid(self):
        self


    def get_challenge_invalid_out_of_range(self):
        self


    def put_challenge_valid(self):
        self


    def delete_challenge_valid(self):
        self


    def delete_challenge_invalid(self):
        self

