import datetime
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from apps.achievements.models import Achievement


class AchievementsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="admin", password="password123")
        self.ach = Achievement.objects.create(
            title="Winner - National Hackathon 2025",
            organization="Tech Hub",
            date=datetime.date(2025, 9, 1),
            active=True
        )

    def test_str_and_public_view(self):
        self.assertEqual(str(self.ach), "Winner - National Hackathon 2025")
        resp = self.client.get(reverse('public:achievements'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Winner - National Hackathon 2025")

    def test_admin_list_view(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('achievements:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Winner - National Hackathon 2025")
