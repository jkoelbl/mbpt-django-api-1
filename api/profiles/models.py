from django.db import models
from api.models import Language, Tier
from api.todo.models import Todo


class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    display_name = models.CharField(max_length=150, blank=True)
    image = models.URLField(blank=True)
    default_language = models.ForeignKey(
        Language, related_name='profile', on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='profile',
        on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, null=True)
    tier = models.ForeignKey(Tier, on_delete=models.DO_NOTHING, default=1)
