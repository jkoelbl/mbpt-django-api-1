from django.conf.urls import url
from django.urls import path

from api.challenges.views import ChallengeList, ChallengeDetail

urlpatterns = [
    path('', ChallengeList.as_view()),
    url(r'^(?P<challenge_id>[^/]+)$', ChallengeDetail.as_view(), name='detail')
]
