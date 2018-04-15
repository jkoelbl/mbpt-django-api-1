from django import http
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.profiles.models import Profile
from api.profiles.serializers import ProfileSerializer
#create profile if no user present, ignore otherwise
#assume info is sent as json

class ProfileDetail(APIView):
    def get_object(self, user):
        try:
            return Profile.objects.get(owner=user)
        except Profile.DoesNotExist:
            return None

    def get(self, request, format=None):
        profile = self.get_object(request.user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        profile = self.get_object(user=request.user)

        if profile is not None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = ProfileSerializer(profile, data=request.data)

        if serializer.is_valid():
            profile = Profile.objects.create(
                title=serializer.validated_data['title'],
                content=serializer.validated_data['content'],
                owner=request.user
            )
            profile.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
