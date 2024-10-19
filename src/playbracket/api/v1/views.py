from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from playbracket.api.v1.serializers import (
    PlayerSerializer,
    LeagueSerializer,
    SportSerializer,
    MatchSerializer,
    EventSerializer,
)
from playbracket.models import (
    Player,
    Sport,
    Event,
    League,
    Match
)


class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Player.objects.all()


class LeagueViewSet(viewsets.ModelViewSet):
    serializer_class = LeagueSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = League.objects.all()


class SportViewSet(viewsets.ModelViewSet):
    serializer_class = SportSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Sport.objects.all()


class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Match.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()
