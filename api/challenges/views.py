from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response

from api.challenges.models import Challenge, Submission
from api.challenges.serializers import ChallengeListSerializer, ChallengeDetailSerializer, SubmissionListSerializer


class ChallengeList(ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeListSerializer


class ChallengeDetail(RetrieveAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeDetailSerializer
    lookup_field = 'challenge_id'


class SubmissionList(ListAPIView):
    def get(self, request, challenge_id):
        # get the country by its primary key from the url
        challenge = Challenge.objects.get(challenge_id=challenge_id)
        submissions = Submission.objects.filter(challenge=challenge)
        serializer = SubmissionListSerializer(submissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
