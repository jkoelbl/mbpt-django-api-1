from django.conf.urls import url

from challenges.views import ChallengeList

urlpatterns = [
    url(r'^', ChallengeList.as_view())
]