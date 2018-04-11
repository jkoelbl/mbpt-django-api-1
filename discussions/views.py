from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from discussions.models import Discussion
from discussions.serializers import DiscussionSerializer


class DiscussionList(ListCreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)

class DiscussionDetail(RetrieveUpdateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)