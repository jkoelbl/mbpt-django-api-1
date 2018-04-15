from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from api.announcements.models import Announcement
from api.announcements.serializers import AnnouncementListSerializer, AnnouncementDetailSerializer


class AnnouncementList(ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementListSerializer


class AnnouncementDetail(RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementDetailSerializer
