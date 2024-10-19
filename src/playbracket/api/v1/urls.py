from django.urls import path, include
from .views import (
    PlayerViewSet,
    SportViewSet,
    EventViewSet,
    LeagueViewSet,
    MatchViewSet,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"players", PlayerViewSet)
router.register(r"sports", SportViewSet)
router.register(r"events", EventViewSet)
router.register(r"leagues", LeagueViewSet)
router.register(r"matches", MatchViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
