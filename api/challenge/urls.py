from django.conf.urls import url

from api.challenge.views import ChallengeList

urlpatterns = [
    url(r'^', ChallengeList.as_view())
]