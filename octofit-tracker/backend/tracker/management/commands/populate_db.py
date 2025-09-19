from django.core.management.base import BaseCommand
from tracker.models import User, Team, Workout, Activity, LeaderboardEntry
from django.db import transaction


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        # Delete in dependency order to avoid relational issues
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Workout.objects.all().delete()
        # djongo が WHERE NOT を含む一括削除で失敗するためループで削除
        for u in User.objects.all():
            if not u.is_superuser:
                u.delete()
        Team.objects.all().delete()

        self.stdout.write(self.style.WARNING('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel heroes team')
        dc = Team.objects.create(name='DC', description='DC heroes team')

        self.stdout.write(self.style.WARNING('Creating users (heroes)...'))
        heroes = [
            ("ironman", "ironman@example.com", marvel),
            ("captainamerica", "cap@example.com", marvel),
            ("thor", "thor@example.com", marvel),
            ("spiderman", "spidey@example.com", marvel),
            ("batman", "batman@example.com", dc),
            ("superman", "superman@example.com", dc),
            ("wonderwoman", "wonderwoman@example.com", dc),
            ("flash", "flash@example.com", dc),
        ]
        user_objs = []
        for username, email, team in heroes:
            u = User.objects.create_user(username=username, email=email, password='password123', team=team)
            user_objs.append(u)

        self.stdout.write(self.style.WARNING('Creating workouts...'))
        workouts = [
            ("Strength Circuit", "Full body strength routine", "medium"),
            ("HIIT Blast", "High intensity interval training", "hard"),
            ("Mobility Flow", "Flexibility and mobility focus", "easy"),
        ]
        workout_objs = [Workout.objects.create(title=t, description=d, difficulty=diff) for t, d, diff in workouts]

        self.stdout.write(self.style.WARNING('Logging activities...'))
        for i, user in enumerate(user_objs):
            Activity.objects.create(
                user=user,
                workout=workout_objs[i % len(workout_objs)],
                activity_type='training',
                duration_minutes=30 + (i * 5),
                calories=200 + (i * 20),
            )

        self.stdout.write(self.style.WARNING('Creating leaderboard entries...'))
        for user in user_objs:
            LeaderboardEntry.objects.create(user=user, team=user.team, score=user.activities.count() * 100, period='weekly')

        self.stdout.write(self.style.SUCCESS('Database populated with sample hero data.'))
