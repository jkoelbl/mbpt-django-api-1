from django.conf.urls import url
from django.urls import path

from api.announcements.views import AnnouncementList, AnnouncementDetail

urlpatterns = [
    path('', AnnouncementList.as_view()),
    url(r'^(?P<pk>[^/]+)$', AnnouncementDetail.as_view())
]
