from django.db import models


class Discussion(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    publisher = models.ForeignKey(
        'auth.User',
        related_name='discussion',
        on_delete=models.CASCADE)
