from django.contrib import admin
from .models import User, Team, Workout, Activity, LeaderboardEntry


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ("username", "email", "team", "is_staff", "is_superuser")
	search_fields = ("username", "email")
	list_filter = ("team", "is_staff", "is_superuser")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ("name", "description")
	search_fields = ("name",)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
	list_display = ("title", "difficulty")
	search_fields = ("title",)
	list_filter = ("difficulty",)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ("user", "activity_type", "duration_minutes", "calories", "performed_at")
	search_fields = ("user__username", "activity_type")
	list_filter = ("activity_type", "performed_at")


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
	list_display = ("user", "team", "score", "period", "updated_at")
	list_filter = ("period", "team")
