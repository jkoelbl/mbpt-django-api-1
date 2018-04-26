from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from api.discussions.models import *
from api.models import Tag
from api.serializers import TagSerializer


class CommentListSerializer(serializers.ModelSerializer):
    display_name = serializers.ReadOnlyField(source='profile.display_name')
    image = serializers.ReadOnlyField(source='profile.image')

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created', 'display_name',
                  'image', 'upvotes')


class CommentDetailSerializer(serializers.ModelSerializer):
    display_name = serializers.ReadOnlyField(source='profile.display_name')
    image = serializers.ReadOnlyField(source='profile.image')
    parent_comment = SerializerMethodField()
    upvoted = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created', 'display_name', 'image', 'upvoted',
                  'upvotes', 'parent_comment')

    def get_parent_comment(self, obj):
        if obj.parent_comment is not None:
            return CommentDetailSerializer(obj.parent_comment, context=self.context).data
        else:
            return None

    def get_upvoted(self, obj):
        try:
            user = self.context.get('user')
            profile = Profile.objects.get(owner=user)
            Upvote.objects.get(profile=profile, comment=obj)
            return True
        except:
            pass
        return False


class CommentIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id',)


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
    comments = SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)
    upvoted = SerializerMethodField()

    class Meta:
        model = Discussion
        fields = ('id', 'title', 'created', 'display_name', 'image', 'upvoted',
                  'view_count', 'upvotes', 'content', 'comments', 'tags')

    def get_comments(self, obj):
        return CommentDetailSerializer(obj.comments, many=True, read_only=True, context=self.context).data

    def get_upvoted(self, obj):
        return self.context.get('upvoted')
