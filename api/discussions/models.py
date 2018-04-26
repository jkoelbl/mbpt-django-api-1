from django.db import models

from api.models import Tag
from api.profiles.models import Profile


class Discussion(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(
        Profile,
        related_name='discussion',
        on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)


class Comment(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(
        Profile,
        related_name='comment',
        on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    parent_comment = models.ForeignKey('self', blank=True, null=True,
        related_name="comment", on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, blank=True, null=True,
        related_name="comments", on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)


class Upvote(models.Model):
    profile = models.ForeignKey(
        Profile,
        related_name='profile',
        on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, blank=True, null=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.CASCADE)
