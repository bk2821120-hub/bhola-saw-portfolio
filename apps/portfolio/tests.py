from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from apps.portfolio.models import Profile, WebsiteSetting, SocialLink


class PortfolioPublicViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile = Profile.objects.create(
            name="Bhola Kumar",
            professional_title="Full-Stack Developer",
            short_intro="Developer intro",
            email="bhola@example.com"
        )
        self.settings = WebsiteSetting.objects.create(
            site_name="Bhola Portfolio",
            primary_color="#6366f1",
            secondary_color="#8b5cf6"
        )
        self.social = SocialLink.objects.create(
            platform="github",
            url="https://github.com",
            icon="bi-github",
            active=True
        )

    def test_home_page_status_and_context(self):
        response = self.client.get(reverse('public:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bhola Kumar")
        self.assertContains(response, "Full-Stack Developer")

    def test_about_page_status(self):
        response = self.client.get(reverse('public:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About Me")

    def test_resume_fallback_when_no_resume(self):
        response = self.client.get(reverse('public:resume'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Resume Not Uploaded Yet")

    def test_maintenance_mode_middleware(self):
        self.settings.maintenance_mode = True
        self.settings.save()

        # Anonymous visitors receive 503
        anon_resp = self.client.get(reverse('public:home'))
        self.assertEqual(anon_resp.status_code, 503)
        self.assertContains(anon_resp, "Under Scheduled Maintenance", status_code=503)

        # Login page is still accessible
        login_resp = self.client.get(reverse('accounts:login'))
        self.assertEqual(login_resp.status_code, 200)

        # Authenticated staff user bypasses maintenance mode
        staff_user = User.objects.create_user(username="staff", password="password", is_staff=True)
        self.client.force_login(staff_user)
        auth_resp = self.client.get(reverse('public:home'))
        self.assertEqual(auth_resp.status_code, 200)

    def test_portal_views_require_login(self):
        anon_client = Client()
        resp = anon_client.get(reverse('portfolio_admin:profile'))
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(resp.url.startswith(reverse('accounts:login')))
