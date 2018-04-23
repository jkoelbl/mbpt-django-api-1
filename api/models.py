from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    phrase = models.CharField(max_length=100)
