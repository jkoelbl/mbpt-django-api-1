from django.db import models


class Profile(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='profile',
        on_delete=models.CASCADE)
