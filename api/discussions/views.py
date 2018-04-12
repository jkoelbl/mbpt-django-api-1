from rest_framework.generics import ListCreateAPIView
from api.discussions.models import Discussion
from api.discussions.serializers import DiscussionSerializer


class DiscussionList(ListCreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)
