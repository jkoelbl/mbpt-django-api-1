from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView
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
            profile = Profile.objects.get(owner=self.request.user)
            discussion.save(profile=profile)


class DiscussionDetail(RetrieveUpdateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionDetailSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(owner=self.request.user)
        serializer.save(profile=profile)
