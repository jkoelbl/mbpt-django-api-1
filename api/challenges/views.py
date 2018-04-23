from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.challenges.models import Challenge, Submission, SubmissionStatus
from api.challenges.serializers import ChallengeListSerializer, ChallengeDetailSerializer, SubmissionListSerializer, \
    SubmissionDetailSerializer


class ChallengeList(ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeListSerializer


class ChallengeDetail(RetrieveAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeDetailSerializer
    lookup_field = 'challenge_id'


class SubmissionListCreate(APIView):
    def get(self, request, challenge_id):
        # get the country by its primary key from the url
        challenge = Challenge.objects.get(challenge_id=challenge_id)
        submissions = Submission.objects.filter(challenge=challenge)
        serializer = SubmissionListSerializer(submissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, challenge_id, filename=None, format=None):
        submission = SubmissionDetailSerializer(data=request.data)
        if submission.is_valid():
            submission.save(
                owner=request.user,
                challenge=Challenge.objects.get(challenge_id=challenge_id),
                status=SubmissionStatus.objects.get(id=1)
            )
            return Response(submission.validated_data, status=status.HTTP_201_CREATED)
        return Response(status=400)



class SubmissionList(APIView):
    def get(self, request):
        # get the country by its primary key from the url
        submissions = Submission.objects.filter(owner=request.user)
        serializer = SubmissionListSerializer(submissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
