from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

User = get_user_model()

class AnnouncementTest(TestCase):

    def setUp(self):
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.username = 'test_user'
        self.email = 'test_user@csumb.edu'
        self.password = 'test_user_password'
        self.user = User.objects.create_user(self.username, self.email, self.password)



    def get_announcements(self):
        self


    def post_announcements(self):
        self


    def get_announcement_valid(self):
        self


    def get_announcement_invalid_out_of_range(self):
        self


    def put_announcement_valid(self):
        self


    def delete_announcement_valid(self):
        self


    def delete_announcement_invalid(self):
        self

