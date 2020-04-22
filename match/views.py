from rest_framework import generics

from match.models import Match
from match.serializers import MatchSerializer


class MatchListView(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    http_method_names = ['get']


class MatchDetailView(generics.RetrieveAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    http_method_names = ['get']
    lookup_field = 'human_id'
