from django.db import models


class Challenge(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    publisher = models.ForeignKey(
        'auth.User',
        related_name='challenge',
        on_delete=models.CASCADE)
