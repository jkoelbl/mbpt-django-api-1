from django.conf.urls import url
from django.urls import path

from api.discussions.views import *

urlpatterns = [
    path('', DiscussionList.as_view()),
    url(r'^profile/$', DiscussionProfile.as_view()),
    url(r'^(?P<pk>[^/]+)$', DiscussionDetail.as_view()),
    url(r'^(?P<pk>[^/]+)/upvote$', DiscussionUpvote.as_view()),
    url(r'^comment/$', CommentList.as_view()),
    url(r'^comment/profile/$', CommentProfile.as_view()),
    url(r'^comment/(?P<pk>[^/]+)$', CommentDetail.as_view()),
    url(r'^comment/(?P<pk>[^/]+)/upvote$', CommentUpvote.as_view())
]
