from rest_framework import serializers
from .models import User, Team, Workout, Activity, LeaderboardEntry


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description']


class UserSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), source='team', write_only=True, required=False, allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'team', 'team_id']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'title', 'description', 'difficulty']


class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    workout = WorkoutSerializer(read_only=True)
    workout_id = serializers.PrimaryKeyRelatedField(queryset=Workout.objects.all(), source='workout', write_only=True, required=False, allow_null=True)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'workout', 'workout_id', 'activity_type', 'duration_minutes', 'calories', 'performed_at']


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), source='team', write_only=True, required=False, allow_null=True)

    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'user', 'user_id', 'team', 'team_id', 'score', 'period', 'updated_at']
