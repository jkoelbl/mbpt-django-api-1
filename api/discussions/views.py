from django.http import Http404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.discussions.serializers import *


class CommentProfile(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.get(owner=request.user)
        comments = Comment.objects.filter(profile=profile)
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentList(APIView):
    def post(self, request, format=None):
        profile = Profile.objects.get(owner=request.user)
        serializer = CommentDetailSerializer(data=request.data, context={
            'user': request.user
        })
        if serializer.is_valid():
            discussion = Discussion.objects.get(id=request.data['discussion'])
            try:
                comment = Comment.objects.get(id=request.data['comment'])
                serializer.save(
                    profile=profile,
                    discussion=discussion,
                    parent_comment=comment
                )
            except KeyError:
                serializer.save(profile=profile, discussion=discussion)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentDetailSerializer(comment, context={
            'user': request.user
        })
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        profile = Profile.objects.get(owner=request.user)
        comment = self.get_object(pk)
        serializer = CommentDetailSerializer(comment, data=request.data, context={
            'user': request.user
        })
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)


class DiscussionProfile(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.get(owner=request.user)
        discussions = Discussion.objects.filter(profile=profile)
        serializer = DiscussionListSerializer(discussions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
            serializer = DiscussionDetailSerializer(discussion, context={
                'user': request.user,
                'upvoted': upvoted
            })
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Discussion.DoesNotExist:
            pass
        return Response(status=400)


class CommentUpvote(APIView):
    def put(self, request, pk, *args, **kwargs):
        #check for comment in database
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        #get upvote from user profile
        profile = Profile.objects.get(owner=request.user)
        try:
            upvote = Upvote.objects.get(profile=profile, comment_id=pk)
            upvote.delete()
            comment.upvotes -= 1
        except Upvote.DoesNotExist:
            upvote = Upvote.objects.create(
                profile=profile,
                comment=comment,
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
        profile = Profile.objects.get(owner=request.user)
        try:
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
