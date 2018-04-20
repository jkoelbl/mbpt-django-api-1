from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100)
    icon = models.URLField()

class Tag(models.Model):
    phrase = models.CharField(max_length=100)
