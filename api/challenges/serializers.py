from rest_framework import serializers

from api.challenges.models import Challenge


class ChallengeListSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')

    class Meta:
        model = Challenge
        fields = ('challenge_id', 'title', 'description', 'created',
                  'publisher', 'submission_count', 'accepted_count')


class ChallengeDetailSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')

    class Meta:
        model = Challenge
        fields = ('title', 'description', 'created',
                  'publisher', 'content')
