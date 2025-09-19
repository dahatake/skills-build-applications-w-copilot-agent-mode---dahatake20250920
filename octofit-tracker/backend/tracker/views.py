from rest_framework import viewsets
from .models import User, Team, Workout, Activity, LeaderboardEntry
from .serializers import (
    UserSerializer,
    TeamSerializer,
    WorkoutSerializer,
    ActivitySerializer,
    LeaderboardEntrySerializer,
)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().select_related('user', 'workout')
    serializer_class = ActivitySerializer


class LeaderboardEntryViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.all().select_related('user', 'team')
    serializer_class = LeaderboardEntrySerializer
from django.shortcuts import render

# Create your views here.
