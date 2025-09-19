from django.db import models
from django.contrib.auth.models import AbstractUser


class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name


class User(AbstractUser):
	# Username retained but email must be unique; we'll enforce via unique index in Mongo and Django constraint
	email = models.EmailField(unique=True)
	team = models.ForeignKey(Team, related_name="members", null=True, blank=True, on_delete=models.SET_NULL)

	REQUIRED_FIELDS = ["email"]

	def __str__(self):
		return self.username


class Workout(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True)
	difficulty = models.CharField(max_length=30, blank=True)

	def __str__(self):
		return self.title


class Activity(models.Model):
	user = models.ForeignKey(User, related_name="activities", on_delete=models.CASCADE)
	workout = models.ForeignKey(Workout, related_name="activities", null=True, blank=True, on_delete=models.SET_NULL)
	activity_type = models.CharField(max_length=50)
	duration_minutes = models.PositiveIntegerField()
	calories = models.PositiveIntegerField(default=0)
	performed_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} {self.activity_type} {self.duration_minutes}m"


class LeaderboardEntry(models.Model):
	user = models.ForeignKey(User, related_name="leaderboard_entries", on_delete=models.CASCADE)
	team = models.ForeignKey(Team, related_name="leaderboard_entries", null=True, blank=True, on_delete=models.SET_NULL)
	score = models.IntegerField(default=0)
	period = models.CharField(max_length=20, default="weekly")
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = ("user", "period")

	def __str__(self):
		return f"{self.user.username} {self.period} {self.score}"

