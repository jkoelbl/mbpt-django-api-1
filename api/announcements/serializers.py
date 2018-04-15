from rest_framework import serializers

from api.announcements.models import Announcement


class AnnouncementListSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')

    class Meta:
        model = Announcement
        fields = ('id', 'title', 'created', 'publisher')


class AnnouncementDetailSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')

    class Meta:
        model = Announcement
        fields = ('id', 'title', 'content', 'created', 'publisher')