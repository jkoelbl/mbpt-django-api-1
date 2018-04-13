from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.discussions.models import Discussion
from api.discussions.serializers import DiscussionListSerializer, DiscussionDetailSerializer


class DiscussionList(ListCreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionListSerializer

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)


class DiscussionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionDetailSerializer

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)
