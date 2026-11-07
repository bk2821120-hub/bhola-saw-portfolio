import datetime
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from apps.certifications.models import Certification


class CertificationsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="admin", password="password123")
        self.cert = Certification.objects.create(
            name="AWS Certified Solutions Architect",
            organization="Amazon Web Services",
            issue_date=datetime.date(2025, 1, 1),
            active=True
        )

    def test_str_and_public_view(self):
        self.assertIn("AWS Certified", str(self.cert))
        resp = self.client.get(reverse('public:certifications'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "AWS Certified Solutions Architect")

    def test_cert_toggle(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('certifications:toggle', kwargs={'pk': self.cert.pk}))
        self.assertEqual(resp.status_code, 302)
        self.cert.refresh_from_db()
        self.assertFalse(self.cert.active)
