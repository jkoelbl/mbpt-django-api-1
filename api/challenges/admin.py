from django.contrib import admin
from api.challenges.models import Challenge


class ChallengeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Challenge, ChallengeAdmin)
