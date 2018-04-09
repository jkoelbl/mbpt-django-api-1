from rest_framework import serializers

from api.challenge.models import Challenge


class ChallengeSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')

    class Meta:
        model = Challenge
        fields = ('id', 'title', 'description', 'publisher')
