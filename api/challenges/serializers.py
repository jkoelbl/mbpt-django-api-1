from rest_framework import serializers

from api.challenges.models import Challenge, Submission
from api.serializers import TagSerializer


class ChallengeListSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')

    class Meta:
        model = Challenge
        fields = ('challenge_id', 'title', 'description', 'created',
                  'publisher', 'submission_count', 'accepted_count')


class ChallengeDetailSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')
    #for demo porpoises
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Challenge
        fields = ('title', 'description', 'created',
                  'publisher', 'content', 'tags')


class SubmissionListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    status = serializers.ReadOnlyField(source='status.status')
    challenges = ChallengeListSerializer(read_only=True)

    class Meta:
        model = Submission
        fields = ('id', 'created', 'owner', 'challenges', 'status')
