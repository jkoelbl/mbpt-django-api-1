from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from api.discussions.models import *
from api.models import Tag
from api.serializers import TagSerializer


class CommentSerializer(serializers.ModelSerializer):
    display_name = serializers.ReadOnlyField(source='profile.display_name')
    image = serializers.ReadOnlyField(source='profile.image')
    parent_comment = SerializerMethodField()
    upvoted = serializers.BooleanField(default=False)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created', 'display_name', 'image', 'upvoted',
                  'upvotes', 'parent_comment')

    def get_parent_comment(self, obj):
        if obj.parent_comment is not None:
            return CommentSerializer(obj.parent_comment).data
        else:
            return None


class DiscussionListSerializer(serializers.ModelSerializer):
    display_name = serializers.ReadOnlyField(source='profile.display_name')
    image = serializers.ReadOnlyField(source='profile.image')
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Discussion
        fields = ('id', 'title', 'created', 'display_name', 'image',
                  'view_count', 'upvotes', 'tags')


class DiscussionDetailSerializer(serializers.ModelSerializer):
    display_name = serializers.ReadOnlyField(source='profile.display_name')
    image = serializers.ReadOnlyField(source='profile.image')
    comments = CommentSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    upvoted = serializers.BooleanField(default=False)

    class Meta:
        model = Discussion
        fields = ('id', 'title', 'created', 'display_name', 'image', 'upvoted',
                  'view_count', 'upvotes', 'content', 'comments', 'tags')
