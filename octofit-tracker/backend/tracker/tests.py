from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Team, User


class APIRootTests(TestCase):
	def setUp(self):
		self.client = APIClient()

	def test_api_root_available(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, status.HTTP_200_OK)
		self.assertIn('users', resp.json())


class UsersEndpointTests(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.team = Team.objects.create(name='TestTeam')
		User.objects.create_user(username='tester', email='tester@example.com', password='pass1234', team=self.team)

	def test_list_users(self):
		resp = self.client.get('/users/')
		self.assertEqual(resp.status_code, status.HTTP_200_OK)
		self.assertGreaterEqual(len(resp.json()), 1)
