from django.conf.urls import url

from announcements.views import AnnouncementList, AnnouncementDetail

urlpatterns = [
    url(r'^', AnnouncementList.as_view()),
    url(r'^(?P<announcement_id>[^/]+)$', AnnouncementDetail.as_view(), name='detail')
]