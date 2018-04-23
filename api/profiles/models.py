from django.db import models
from api.models import Language, Tier


class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    display_name = models.CharField(max_length=150, blank=True)
    image = models.URLField(blank=True)
    default_language = models.ForeignKey(
        Language, related_name='profile', on_delete=models.CASCADE, default=1)
    owner = models.ForeignKey(
        'auth.User',
        related_name='profile',
        on_delete=models.CASCADE)
    tier = models.ForeignKey(
        Tier, on_delete=models.DO_NOTHING(0,0,0,0), default=1)
