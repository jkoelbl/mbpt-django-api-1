from django.db import models

from api.challenges.models import Challenge


class Todo(models.Model):
    owner = models.ForeignKey(
        'auth.User',
        related_name='todo',
        on_delete=models.CASCADE)
    challenges = models.ManyToManyField(Challenge)

