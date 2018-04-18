from django.contrib import admin

from api.models import Language


class LanguageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Language, LanguageAdmin)
admin.site.site_title = 'MBPT Admin Panel'
admin.site.site_header = 'MBPT Admin Panel'
