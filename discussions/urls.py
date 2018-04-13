from django.conf.urls import url

from discussions.views import DiscussionList, DiscussionDetail

urlpatterns = [
    url(r'^', DiscussionList.as_view()),
    url(r'^(?P<pk>[^/]+)$', DiscussionDetail.as_view(), name='detail')
]