from rest_framework import serializers

from api.discussions.models import Discussion, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created', 'publisher', 'upvotes')


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
