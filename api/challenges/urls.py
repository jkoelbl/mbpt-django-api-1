from django.conf.urls import url
from django.urls import path

from api.challenges.views import ChallengeList, ChallengeDetail, SubmissionListCreate

urlpatterns = [
    path('', ChallengeList.as_view()),
    url(r'^(?P<challenge_id>[^/]+)$', ChallengeDetail.as_view(), name='detail'),
    # All the submissions relate to current user
    url(r'^submission/(?P<challenge_id>[^/]+)$', SubmissionListCreate.as_view(), name='submissions'),
]
