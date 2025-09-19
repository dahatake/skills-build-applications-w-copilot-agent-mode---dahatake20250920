from rest_framework import routers
from .views import (
    TeamViewSet,
    UserViewSet,
    WorkoutViewSet,
    ActivityViewSet,
    LeaderboardEntryViewSet,
)

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'users', UserViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardEntryViewSet)

urlpatterns = router.urls
