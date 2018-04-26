from rest_framework import serializers

from api.challenges.models import Challenge, Submission
from api.profiles.models import Profile
from api.serializers import TagSerializer, LanguageSerializer, TierSerializer


class ChallengeListSerializer(serializers.ModelSerializer):
    publisher = serializers.SerializerMethodField()

    class Meta:
        model = Challenge
        fields = ('challenge_id', 'title', 'description', 'created',
                  'publisher', 'submission_count', 'accepted_count', 'difficulty')

    def get_publisher(self, obj):
        profile = Profile.objects.get(owner=obj.publisher)
        return profile.display_name


class ChallengeDetailSerializer(serializers.ModelSerializer):
    publisher = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)
    tier = TierSerializer(read_only=True)
    accepted = serializers.SerializerMethodField()
    attempted = serializers.SerializerMethodField()
    todo = serializers.SerializerMethodField()

    class Meta:
        model = Challenge
        fields = ('title', 'description', 'created', 'accepted', 'attempted', 'todo',
                  'publisher', 'content', 'tags', 'tier', 'difficulty')

    def get_accepted(self, obj):
        return self.context.get('accepted')

    def get_attempted(self, obj):
        return self.context.get('attempted')

    def get_todo(self, obj):
        return self.context.get('todo')

    def get_publisher(self, obj):
        profile = Profile.objects.get(owner=obj.publisher)
        return profile.display_name


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


class SubmissionIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ('id',)
