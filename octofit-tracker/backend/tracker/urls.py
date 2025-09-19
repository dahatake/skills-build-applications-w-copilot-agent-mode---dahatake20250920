from rest_framework import routers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import path
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

@api_view(['GET'])
def api_root(request):
    return Response({
        'teams': request.build_absolute_uri('teams/'),
        'users': request.build_absolute_uri('users/'),
        'workouts': request.build_absolute_uri('workouts/'),
        'activities': request.build_absolute_uri('activities/'),
        'leaderboard': request.build_absolute_uri('leaderboard/'),
    })

urlpatterns = [
    path('', api_root, name='api-root'),
] + router.urls
