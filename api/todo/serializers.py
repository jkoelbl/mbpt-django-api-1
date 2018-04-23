from rest_framework import serializers

from api.challenges.serializers import ChallengeListSerializer
from api.todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    challenges = ChallengeListSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = ('challenges',)
