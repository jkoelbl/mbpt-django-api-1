from django.db import models


class Challenge(models.Model):
    challenge_id = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    content = models.TextField()
    submission_count = models.PositiveIntegerField(default=0)
    accepted_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey('auth.User', related_name='challenge', on_delete=models.CASCADE)


class Submission(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='submission', on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, related_name='submission', on_delete=models.CASCADE)
