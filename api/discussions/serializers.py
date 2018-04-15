from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from api.discussions.models import *


class CommentSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')
    parent_comment = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created', 'publisher', 'upvotes', 'parent_comment')

    def get_parent_comment(self, obj):
        if obj.parent_comment is not None:
            return CommentSerializer(obj.parent_comment).data
        else:
            return None


class DiscussionListSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')

    class Meta:
        model = Discussion
        fields = ('id', 'title', 'created', 'publisher', 'view_count', 'upvotes')


class DiscussionDetailSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Discussion
        fields = ('id', 'publisher', 'comments')