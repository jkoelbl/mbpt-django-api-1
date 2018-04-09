from django.conf.urls import url

from api.discussions.views import DiscussionList

urlpatterns = [
    url(r'^', DiscussionList.as_view())
]