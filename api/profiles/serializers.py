from rest_framework import serializers

from api.profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='owner.username')
    first_name = serializers.ReadOnlyField(source='owner.first_name')
    last_name = serializers.ReadOnlyField(source='owner.last_name')
    email = serializers.ReadOnlyField(source='owner.email')
    lang = serializers.ReadOnlyField(source='default_language.name')
    lang_icon = serializers.ReadOnlyField(source='default_language.icon')

    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name',
                  'email', 'title', 'content', 'owner_id', 'lang', 'lang_icon')
