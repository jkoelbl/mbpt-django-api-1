from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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
        serializer.save(publisher=self.request.user)

    def get(self, request, pk):
        try:
            discussion = Discussion.objects.get(pk=pk)
            upvoted = False
            try:
                profile = Profile.objects.get(owner=request.user)
                Upvote.objects.get(profile=profile, discussion=discussion)
                upvoted = True
            except:
                pass
            serializer = DiscussionDetailSerializer(discussion, data={
                'upvoted': upvoted
            }, partial=True)
            if serializer.is_valid():
                return Response(DiscussionDetailSerializer(serializer.save()).data, status=status.HTTP_200_OK)
        except Discussion.DoesNotExist:
            pass
        return Response(status=400)


class CommentUpvote(APIView):
    def put(self, request, pk, *args, **kwargs):
        profile, upvote, comment = any, any, any
        #check for comment in database
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        #get upvote from user profile
        try:
            profile = Profile.objects.get(owner=request.user)
            upvote = Upvote.objects.get(profile=profile, comment_id=pk)
            upvote.delete()
            comment.upvotes -= 1
        except Upvote.DoesNotExist:
            upvote = Upvote.objects.create(
                profile=profile,
                comment_id=comment,
            )
            upvote.save()
            comment.upvotes += 1
        comment.save()
        return Response(status=status.HTTP_200_OK)


class DiscussionUpvote(APIView):
    def put(self, request, pk):
        # check for comment in database
        try:
            discussion = Discussion.objects.get(pk=pk)
        except Discussion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # get upvote from user profile
        try:
            profile = Profile.objects.get(owner=request.user)
            upvote = Upvote.objects.get(profile=profile, discussion=discussion)
            upvote.delete()
            discussion.upvotes -= 1
        except Upvote.DoesNotExist:
            upvote = Upvote.objects.create(
                profile=profile,
                discussion=discussion,
            )
            upvote.save()
            discussion.upvotes += 1
        discussion.save()
        return Response(status=status.HTTP_200_OK)
