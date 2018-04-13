from django.conf.urls import url

from api.profiles.views import ProfileDetail

urlpatterns = [
    url(r'^', ProfileDetail.as_view())
]