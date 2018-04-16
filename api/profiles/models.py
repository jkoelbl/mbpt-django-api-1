from django.db import models

from api.models import Language


class Profile(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    default_language = models.ForeignKey(
        Language, related_name='profile', on_delete=models.CASCADE, default=1)
    owner = models.ForeignKey(
        'auth.User',
        related_name='profile',
        on_delete=models.CASCADE)
