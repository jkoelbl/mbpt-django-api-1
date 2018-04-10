from rest_framework import serializers

from discussions.models import Discussion


class DiscussionSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')

    class Meta:
        model = Discussion
        fields = ('id', 'title', 'content', 'created', 'publisher')
