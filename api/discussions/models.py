from django.db import models


class Discussion(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(
        'auth.User',
        related_name='discussion',
        on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    pass


class Comment(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(
        'auth.User',
        related_name='comment',
        on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    parentComment = models.ForeignKey('self', blank=True, null=True,
        related_name="comment", on_delete=models.CASCADE)
    parentDiscussion = models.ForeignKey(Discussion, blank=True, null=True,
        related_name="subcomment", on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
