from rest_framework import serializers

from api.discussions.models import Discussion


class DiscussionListSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')

    class Meta:
        model = Discussion
        fields = ('id', 'title', 'created', 'publisher', 'view_count', 'upvotes')


class DiscussionDetailSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')

    class Meta:
        model = Discussion
        fields = ('id', 'title', 'content', 'created', 'publisher', 'view_count', 'upvotes')
