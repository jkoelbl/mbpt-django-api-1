from django.contrib import admin
from discussions.models import Discussion


class DiscussionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Discussion, DiscussionAdmin)
