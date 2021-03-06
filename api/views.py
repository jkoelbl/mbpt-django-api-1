from django.contrib.auth.models import User, AnonymousUser
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Language
from api.permissions import PublicEndpoint
from api.profiles.models import Profile
from api.serializers import UserSerializer, LanguageSerializer
from api.todo.models import Todo


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
            User.objects.get(username=request.data['username'])
            return Response('username', status=status.HTTP_409_CONFLICT)
        except User.DoesNotExist:
            pass
        if type(request.user) == AnonymousUser:
            try:
                User.objects.get(email=request.data['email'])
                return Response('email', status=status.HTTP_409_CONFLICT)
            except User.DoesNotExist:
                pass
        else:
            try:
                Profile.objects.get(owner=request.user)
                return Response('profile', status=status.HTTP_409_CONFLICT)
            except Profile.DoesNotExist:
                pass
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if type(request.user) == AnonymousUser:
                user = User.objects.create_user(
                    username=serializer.validated_data['username'],
                    first_name=serializer.validated_data['first_name'],
                    last_name=serializer.validated_data['last_name'],
                    password=request.data['password'],
                    email=serializer.validated_data['email']
                )
                user.save()
            else:
                request.user.username = serializer.validated_data['username']
                request.user.first_name = serializer.validated_data['first_name']
                request.user.last_name = serializer.validated_data['last_name']
                request.user.set_password(request.data['password'])
                request.user.save()
                user = request.user
            todo = Todo.objects.create(owner=user)
            todo.save()
            profile = Profile.objects.create(owner=user, todo=todo)
            profile.display_name = user.username
            profile.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LanguageList(ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
