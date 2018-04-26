from django.conf.urls import url
from django.urls import path

from api.discussions.views import DiscussionProfile, CommentProfile
from api.profiles.views import ProfileDetail

urlpatterns = [
    path(r'^', ProfileDetail.as_view()),
    url(r'^discussion/$', DiscussionProfile.as_view()),
    url(r'^comment/$', CommentProfile.as_view()),
]
