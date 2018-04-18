from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from api.discussions.serializers import *


class CommentList(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class DiscussionList(ListCreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionListSerializer

    def perform_create(self, serializer):
        discussion = DiscussionDetailSerializer(data=self.request.data)
        if discussion.is_valid():
            discussion.save(publisher=self.request.user)


class DiscussionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionDetailSerializer

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)
