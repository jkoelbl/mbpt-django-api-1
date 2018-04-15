from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.profiles.models import Profile
from api.profiles.serializers import ProfileSerializer
from api.serializers import UserSerializer


class ProfileDetail(APIView):
    def get_object(self, user):
        try:
            return Profile.objects.get(owner=user)
        except Profile.DoesNotExist:
            return None

    def get(self, request, format=None):
        profile = self.get_object(request.user)
        if profile is None:
            return Response(
                UserSerializer(request.user).data,
                status=status.HTTP_423_LOCKED)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        profile = self.get_object(user=request.user)

        if profile is not None:
            return Response(status=status.HTTP_404_NOT_FOUND)

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
