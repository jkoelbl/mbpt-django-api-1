from django.conf.urls import url

from announcements.views import AnnouncementList, AnnouncementDetail

urlpatterns = [
    url(r'^', AnnouncementList.as_view()),
    url(r'^(?P<pk>[^/]+)$', AnnouncementDetail.as_view(), name='detail')
]
