from django.contrib import admin
from playbracket.models import Sport, League, Player, Event, Match


class SportAdmin(admin.ModelAdmin):
    pass


class LeagueAdmin(admin.ModelAdmin):
    pass


class PlayerAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


class MatchAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sport, SportAdmin)
admin.site.register(League, LeagueAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Match, MatchAdmin)
