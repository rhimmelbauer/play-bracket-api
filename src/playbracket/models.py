from django.db import models
from django.conf import settings
from datetime import date


class Event(models.Model):
    date = models.DateField(default=date.today(), null=False, blank=False)

    def __str__(self):
        return f"{self.date}"


class Player(models.Model):
    name = models.CharField(max_length=80, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name


class Sport(models.Model):
    name = models.CharField(max_length=80, blank=False, null=False, unique=True)
    players = models.ManyToManyField(Player, blank=True, related_name="players")

    def __str__(self):
        return self.name


class League(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    admins = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="admins")
    sport = models.ForeignKey(Sport, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Match(models.Model):
    date = models.DateField(default=date.today(), null=False, blank=False)
    cleared = models.BooleanField(default=False)
    winners = models.ManyToManyField(Player, blank=True, related_name="winners")
    winner_score = models.IntegerField(blank=True, null=True)
    losers = models.ManyToManyField(Player, blank=True, related_name="losers")
    loser_score = models.IntegerField(blank=True, null=True)
    league = models.ForeignKey(League, related_name="matches", blank=True, null=True, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="matches", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.pk} - {self.date}) " +\
            f"Winners: {[x for x in self.winners.all().values_list("name", flat=True)]}, " +\
            f"Losers: {[x for x in self.losers.all().values_list("name", flat=True)]}"
