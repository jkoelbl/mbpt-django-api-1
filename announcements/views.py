from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from announcements.models import Announcement
from announcements.serializers import AnnouncementSerializer


class AnnouncementList(ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)

class AnnouncementDetail(RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer