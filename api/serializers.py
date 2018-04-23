from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Language, Tag, Tier


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('name', 'icon')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','phrase')


class TierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tier
        fields = ('level','label')
