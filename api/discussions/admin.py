from django.contrib import admin
from api.discussions.models import Discussion, Comment


class DiscussionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Discussion, DiscussionAdmin)


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)