from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import PublicEndpoint
from api.serializers import UserSerializer

class UserDetailGet(APIView):
    def get(self, request, format=None):
        serializer = UserSerializer(request.user)

        return Response(serializer.data)

class UserDetailPost(APIView):
    permission_classes = (PublicEndpoint,)

    def post(self, request, format=None):
        if 'password' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(username=request.data['username'])
            return Response('User already exists', status=status.HTTP_409_CONFLICT)
        except User.DoesNotExist:
            pass

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name'],
                password=request.data['password'],
                email=serializer.validated_data['email']
            )
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)