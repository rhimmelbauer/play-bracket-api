from playbracket.models import Player, Sport, Event, League, Match
from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    sports = serializers.ListField(source="sports_display")

    class Meta:
        model = Player
        fields = "__all__"


class SportSerializer(serializers.ModelSerializer):
    players = serializers.ListField(source='players_display')

    class Meta:
        model = Sport
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    matches = serializers.ListField(source="matches_display")
    players = serializers.ListField(source="players_display")

    class Meta:
        model = Event
        fields = "__all__"


class LeagueSerializer(serializers.ModelSerializer):
    sport = serializers.CharField(source="sport.name")

    class Meta:
        model = League
        fields = "__all__"


class MatchSerializer(serializers.ModelSerializer):
    winners = serializers.ListField(source='winners_display')
    losers = serializers.ListField(source='losers_display')
    league = serializers.CharField(source="league.name")
    event = serializers.CharField(source="event.__str__")

    class Meta:
        model = Match
        fields = "__all__"
