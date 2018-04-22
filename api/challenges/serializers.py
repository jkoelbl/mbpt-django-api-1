from rest_framework import serializers

from api.challenges.models import Challenge, Submission


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


class SubmissionListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    status = serializers.ReadOnlyField(source='status.status')
    challenge_id = serializers.ReadOnlyField(source='challenge.challenge_id')

    class Meta:
        model = Submission
        fields = ('id', 'created', 'owner', 'challenge_id', 'status')


class SubmissionDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    status = serializers.ReadOnlyField(source='status.status')
    challenge_id = serializers.ReadOnlyField(source='challenge.challenge_id')

    class Meta:
        model = Submission
        fields = ('id', 'created', 'owner', 'challenge_id', 'status', 'file')
