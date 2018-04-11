from django.conf.urls import url

from announcements.views import AnnouncementList, AnnouncementDetail

urlpatterns = [
    url(r'^', AnnouncementList.as_view()),
    url(r'^(?P<id>[0-?]+)$', AnnouncementDetail.as_view(), name='detail')
]
