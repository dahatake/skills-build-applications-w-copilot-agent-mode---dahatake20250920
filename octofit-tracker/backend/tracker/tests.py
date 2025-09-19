from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Team, User, Workout, Activity, LeaderboardEntry


class APIRootTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root_available(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        for key in ['users', 'teams', 'workouts', 'activities', 'leaderboard']:
            self.assertIn(key, resp.json())


class BaseDataMixin:
    def create_base_data(self):
        self.team = Team.objects.create(name='TestTeam')
        self.user = User.objects.create_user(username='tester', email='tester@example.com', password='pass1234', team=self.team)
        self.workout = Workout.objects.create(title='Push Ups', description='Upper body', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, activity_type='pushups', duration_minutes=10, calories=50)
        self.leaderboard = LeaderboardEntry.objects.create(user=self.user, team=self.team, period='daily', score=50)


class UsersEndpointTests(TestCase, BaseDataMixin):
    def setUp(self):
        self.client = APIClient()
        self.create_base_data()

    def test_list_users(self):
        resp = self.client.get('/users/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(resp.json()), 1)


class TeamsEndpointTests(TestCase, BaseDataMixin):
    def setUp(self):
        self.client = APIClient()
        self.create_base_data()

    def test_list_teams(self):
        resp = self.client.get('/teams/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(resp.json()), 1)


class WorkoutsEndpointTests(TestCase, BaseDataMixin):
    def setUp(self):
        self.client = APIClient()
        self.create_base_data()

    def test_list_workouts(self):
        resp = self.client.get('/workouts/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(resp.json()), 1)


class ActivitiesEndpointTests(TestCase, BaseDataMixin):
    def setUp(self):
        self.client = APIClient()
        self.create_base_data()

    def test_list_activities(self):
        resp = self.client.get('/activities/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(resp.json()), 1)


class LeaderboardEndpointTests(TestCase, BaseDataMixin):
    def setUp(self):
        self.client = APIClient()
        self.create_base_data()

    def test_list_leaderboard(self):
        resp = self.client.get('/leaderboard/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(resp.json()), 1)
