from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class AccountsAuthTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="owner", password="password123")

    def test_login_successful(self):
        resp = self.client.post(reverse('accounts:login'), {
            'username': 'owner',
            'password': 'password123'
        })
        self.assertRedirects(resp, reverse('accounts:dashboard'))

    def test_login_invalid_credentials(self):
        resp = self.client.post(reverse('accounts:login'), {
            'username': 'owner',
            'password': 'wrongpassword'
        })
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Invalid username or password")

    def test_open_redirect_protection(self):
        # Malicious next URL should be ignored and default to dashboard
        resp = self.client.post(reverse('accounts:login') + '?next=https://malicious-site.com', {
            'username': 'owner',
            'password': 'password123'
        })
        self.assertRedirects(resp, reverse('accounts:dashboard'))

    def test_dashboard_accessible_when_authenticated(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('accounts:dashboard'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Dashboard Overview")

    def test_logout(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('accounts:logout'))
        self.assertRedirects(resp, reverse('accounts:login'))
