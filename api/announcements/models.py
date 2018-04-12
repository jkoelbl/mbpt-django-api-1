from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(
        'auth.User',
        related_name='announcement',
        on_delete=models.CASCADE)

    class Meta:
        app_label = 'announcements'
