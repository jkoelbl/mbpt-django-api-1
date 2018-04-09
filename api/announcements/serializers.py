from rest_framework import serializers

from api.announcements.models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')

    class Meta:
        model = Announcement
        fields = ('id', 'title', 'content', 'publisher')
