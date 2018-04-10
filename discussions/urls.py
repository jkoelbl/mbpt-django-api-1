from django.conf.urls import url

from discussions.views import DiscussionList

urlpatterns = [
    url(r'^', DiscussionList.as_view())
]