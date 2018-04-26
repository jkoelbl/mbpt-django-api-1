from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.challenges.models import Challenge, Submission, SubmissionStatus
from api.challenges.serializers import ChallengeListSerializer, ChallengeDetailSerializer, SubmissionListSerializer, \
    SubmissionDetailSerializer, SubmissionIDSerializer
from api.models import Language
from api.todo.models import Todo


class ChallengeList(ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeListSerializer


class ChallengeDetail(APIView):
    def get(self, request, challenge_id):
        try:
            challenge = Challenge.objects.get(challenge_id=challenge_id)
        except Challenge.DoesNotExist:
            return Response(status=400)
        submissions = challenge.submission_set.filter(owner=request.user)
        accepted = submissions.filter(status=2)
        inTodoList = False
        try:
            todo = Todo.objects.get(owner=request.user)
            todo.challenges.get(challenge_id=challenge_id)
            inTodoList = True
        except:
            pass
        serializer = ChallengeDetailSerializer(challenge, context={
            'accepted': len(accepted) > 0,
            'attempted': len(submissions) > 0,
            'todo': inTodoList
        },)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubmissionListCreate(APIView):
    def get(self, request, challenge_id):
        # get the country by its primary key from the url
        challenge = Challenge.objects.get(challenge_id=challenge_id)
        submissions = Submission.objects.filter(challenge=challenge)
        serializer = SubmissionListSerializer(submissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, challenge_id, filename=None, format=None):
        # increment challenge submission counter
        # only perform this if the user hasn't submitted with acceptance
        challenge = Challenge.objects.get(challenge_id=challenge_id)
        prev_submission = Submission.objects.filter(owner=request.user, challenge_id=challenge)
        if len(prev_submission) == 0:
            challenge.submission_count += 1
            challenge.save()

        serializer = SubmissionDetailSerializer(data=request.data)
        if serializer.is_valid() and 'language_id' in request.data:
            submission = serializer.save(
                owner=request.user,
                challenge=Challenge.objects.get(challenge_id=challenge_id),
                status=SubmissionStatus.objects.get(id=1),
                language=Language.objects.get(id=request.data['language_id'])
            )
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
