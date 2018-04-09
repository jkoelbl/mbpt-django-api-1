from rest_framework.generics import ListCreateAPIView
from api.challenge.models import Challenge
from api.challenge.serializers import ChallengeSerializer


class ChallengeList(ListCreateAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)
