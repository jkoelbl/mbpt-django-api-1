from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from api.announcements.models import Announcement
from api.announcements.serializers import AnnouncementListSerializer, AnnouncementDetailSerializer


class AnnouncementList(ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementListSerializer

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)


class AnnouncementDetail(RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementDetailSerializer
