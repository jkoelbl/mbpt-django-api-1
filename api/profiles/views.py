from django import http
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.profiles.models import Profile
from api.profiles.serializers import ProfileSerializer


class ProfileDetail(APIView):
    def get_object(self, user):
        try:
            return Profile.objects.get(owner=user)
        except Profile.DoesNotExist:
            raise http.Http404

    def get(self, request, format=None):
        profile = self.get_object(request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        return Response(status=status.HTTP_400_BAD_REQUEST)
