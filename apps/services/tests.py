from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from apps.services.models import Service


class ServicesTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="admin", password="password123")
        self.service = Service.objects.create(
            title="Python Data Analysis",
            short_description="Clean and analyze your business datasets with Python",
            deliverables="Data cleaning using Pandas\nExploratory Data Analysis\nData visualization",
            technologies="Python, Pandas, NumPy, Matplotlib, Seaborn",
            icon="bi-filetype-py",
            starting_price="$99",
            is_active=True,
            display_order=1
        )

    def test_slug_generation_and_properties(self):
        self.assertEqual(self.service.slug, "python-data-analysis")
        self.assertEqual(len(self.service.deliverables_list), 3)
        self.assertEqual(len(self.service.technologies_list), 5)

    def test_duplicate_slug_resolution(self):
        dup = Service.objects.create(
            title="Python Data Analysis",
            short_description="Another python data service"
        )
        self.assertEqual(dup.slug, "python-data-analysis-1")

    def test_public_services_page(self):
        resp = self.client.get(reverse('public:services'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Data-Driven Solutions for Your Business")
        self.assertContains(resp, "Python Data Analysis")

    def test_service_toggle_active(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('services:toggle', kwargs={'pk': self.service.pk}))
        self.assertEqual(resp.status_code, 302)
        self.service.refresh_from_db()
        self.assertFalse(self.service.is_active)
