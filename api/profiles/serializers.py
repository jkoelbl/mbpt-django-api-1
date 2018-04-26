from rest_framework import serializers

from api.profiles.models import Profile
from api.serializers import TierSerializer, LanguageSerializer


class ProfileListSerializer(serializers.ModelSerializer):
    default_language = LanguageSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('display_name', 'default_language', 'image', 'points')

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='owner.username')
    first_name = serializers.ReadOnlyField(source='owner.first_name')
    last_name = serializers.ReadOnlyField(source='owner.last_name')
    email = serializers.ReadOnlyField(source='owner.email')
    default_language = LanguageSerializer(read_only=True)
    tier = TierSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('username', 'display_name', 'first_name', 'last_name',
                  'email', 'owner_id', 'default_language', 'image', 'tier')
