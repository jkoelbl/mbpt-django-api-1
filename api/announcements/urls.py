from django.conf.urls import url

from api.announcements.views import AnnouncementList

urlpatterns = [
    url(r'^', AnnouncementList.as_view())
]