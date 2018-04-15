from django.conf.urls import url
from django.urls import path

from api.discussions.views import *

urlpatterns = [
    path('', DiscussionList.as_view()),
    url(r'^(?P<pk>[^/]+)$', DiscussionDetail.as_view()),
    url(r'^comment/(?P<pk>[^/]+)$', CommentList.as_view())
]
