import datetime
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from apps.experience.models import Experience
from apps.experience.forms import ExperienceForm


class ExperienceTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="admin", password="password123")
        self.exp = Experience.objects.create(
            company="Tech Labs",
            position="Software Engineer",
            employment_type="full_time",
            start_date=datetime.date(2024, 1, 1),
            currently_working=True,
            responsibilities="Developed Django APIs\nOptimized MySQL queries",
            skills_used="Python, Django, MySQL",
            active=True
        )

    def test_model_properties(self):
        self.assertEqual(self.exp.end_display, "Present")
        self.assertEqual(len(self.exp.responsibilities_list), 2)
        self.assertEqual(self.exp.skills_list, ["Python", "Django", "MySQL"])

    def test_form_date_validation(self):
        form = ExperienceForm(data={
            'company': 'Tech Labs',
            'position': 'Engineer',
            'employment_type': 'full_time',
            'start_date': datetime.date(2025, 1, 1),
            'end_date': datetime.date(2024, 1, 1),  # Earlier than start
            'currently_working': False,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('end_date', form.errors)

    def test_public_experience_view(self):
        resp = self.client.get(reverse('public:experience'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Software Engineer")
        self.assertContains(resp, "Tech Labs")
