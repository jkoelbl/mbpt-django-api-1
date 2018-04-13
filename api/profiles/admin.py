from django.contrib import admin
from api.profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
