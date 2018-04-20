from django.db import models


class Challenge(models.Model):
    challenge_id = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    content = models.TextField()
    difficulty = models.IntegerField(default=0)
    submission_count = models.PositiveIntegerField(default=0)
    accepted_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey('auth.User', related_name='challenge', on_delete=models.CASCADE)


class SubmissionStatus(models.Model):
    status = models.CharField(max_length=64)


class Submission(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='submission', on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, related_name='submission', on_delete=models.CASCADE)
    status = models.ForeignKey(SubmissionStatus, related_name='submission', on_delete=models.CASCADE)

