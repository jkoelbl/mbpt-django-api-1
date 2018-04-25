from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.challenges.models import Challenge, Submission, SubmissionStatus
from api.challenges.serializers import ChallengeListSerializer, ChallengeDetailSerializer, SubmissionListSerializer, \
    SubmissionDetailSerializer, SubmissionIDSerializer
from api.models import Language


class ChallengeList(ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeListSerializer


class ChallengeDetail(RetrieveUpdateAPIView):
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
        serializer = SubmissionDetailSerializer(data=request.data)
        if serializer.is_valid() and 'language_id' in request.data:
            submission = serializer.save(
                owner=request.user,
                challenge=Challenge.objects.get(challenge_id=challenge_id),
                status=SubmissionStatus.objects.get(id=1),
                language=Language.objects.get(id=request.data['language_id'])
            )
            #increment challenge submission and acceptance counters
            #only perform this if the user hasn't submitted with acceptance
            prev_submission = Submission.objects.filter(owner=request.user).filter(status_id=1)
            if len(prev_submission) == 0:
                challenge = Challenge.objects.get(challenge_id=challenge_id)
                challenge.submission_count += 1
                if submission.status_id == 1:
                    challenge.accepted_count += 1
                challenge.save()

            return Response(SubmissionIDSerializer(submission).data, status=status.HTTP_201_CREATED)
        return Response(status=400)


class SubmissionList(APIView):
    def get(self, request):
        # get the country by its primary key from the url
        submissions = Submission.objects.filter(owner=request.user)
        serializer = SubmissionListSerializer(submissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubmissionDetail(RetrieveAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionDetailSerializer

    def get(self, request, *args, **kwargs):
        submission = self.get_object()
        if submission.owner.id != request.user.id:
            return Response(status=400)
        serializer = self.get_serializer(submission)
        return Response(serializer.data)
