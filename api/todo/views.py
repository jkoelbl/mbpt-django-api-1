from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.challenges.models import Challenge
from api.todo.models import Todo
from api.todo.serializers import TodoSerializer


class TodoList(APIView):
    def get(self, request, format=None):
        try:
            todo = Todo.objects.get(owner=request.user)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Todo.DoesNotExist:
            todo = Todo.objects.create(
                owner = request.user
            )
            todo.save()
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, format=None):
        try:
            challenge = Challenge.objects.get(challenge_id=request.data['challenge_id'])
        except Challenge.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        todo = Todo.objects.get(owner=request.user)
        todo.challenges.add(challenge)
        todo.save()
        return Response(status=status.HTTP_200_OK)