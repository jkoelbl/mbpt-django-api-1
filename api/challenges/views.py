from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from api.challenges.models import Challenge
from api.challenges.serializers import ChallengeListSerializer, ChallengeDetailSerializer


class ChallengeList(ListCreateAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeListSerializer

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)


class ChallengeDetail(RetrieveAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeDetailSerializer
    lookup_field = 'challenge_id'
