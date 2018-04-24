from rest_framework import serializers

from api.challenges.models import Challenge, Submission
from api.serializers import TagSerializer, LanguageSerializer, TierSerializer


class ChallengeListSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')

    class Meta:
        model = Challenge
        fields = ('challenge_id', 'title', 'description', 'created',
                  'publisher', 'submission_count', 'accepted_count', 'difficulty')


class ChallengeDetailSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')
    tags = TagSerializer(many=True, read_only=True)
    tier = TierSerializer(read_only=True)

    class Meta:
        model = Challenge
        fields = ('title', 'description', 'created',
                  'publisher', 'content', 'tags', 'tier', 'difficulty')


class SubmissionListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    status = serializers.ReadOnlyField(source='status.status')
    challenge_id = serializers.ReadOnlyField(source='challenge.challenge_id')
    language = LanguageSerializer(read_only=True)

    class Meta:
        model = Submission
        fields = ('id', 'created', 'owner', 'challenge_id', 'status', 'language')


class SubmissionDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    status = serializers.ReadOnlyField(source='status.status')
    challenge_id = serializers.ReadOnlyField(source='challenge.challenge_id')
    language = LanguageSerializer(read_only=True)

    class Meta:
        model = Submission
        fields = ('id', 'created', 'owner', 'challenge_id', 'status', 'content', 'language')
