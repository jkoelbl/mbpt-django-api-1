from django.contrib import admin
from django.contrib.auth.models import User
from oauth2_provider.admin import AccessToken, Application, RefreshToken, Grant
from social_django.admin import Association, Nonce, UserSocialAuth

from api.models import Language


class LanguageAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(User)
admin.site.unregister(AccessToken)
admin.site.unregister(Application)
admin.site.unregister(RefreshToken)
admin.site.unregister(Grant)
admin.site.unregister(Association)
admin.site.unregister(Nonce)
admin.site.unregister(UserSocialAuth)
admin.site.register(Language, LanguageAdmin)
admin.site.site_title = 'MBPT Admin Panel'
admin.site.site_header = 'MBPT Admin Panel'
