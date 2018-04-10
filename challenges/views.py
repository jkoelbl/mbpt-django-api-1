from rest_framework.generics import ListCreateAPIView
from challenges.models import Challenge
from challenges.serializers import ChallengeSerializer


class ChallengeList(ListCreateAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)
