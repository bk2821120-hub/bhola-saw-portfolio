from django.test import TestCase, Client
from django.urls import reverse
from apps.education.models import Education
from apps.education.forms import EducationForm


class EducationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.edu = Education.objects.create(
            degree="B.Tech Computer Science",
            institution="National Institute of Technology",
            start_year=2021,
            end_year=2025,
            result="8.8 CGPA",
            active=True
        )

    def test_duration_property(self):
        self.assertIn("2021", self.edu.duration)
        self.assertIn("2025", self.edu.duration)

    def test_form_year_validation(self):
        form = EducationForm(data={
            'degree': 'M.Tech',
            'institution': 'University',
            'start_year': 2025,
            'end_year': 2022,  # earlier than start year
        })
        self.assertFalse(form.is_valid())
        self.assertIn('end_year', form.errors)

    def test_public_education_view(self):
        resp = self.client.get(reverse('public:education'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "B.Tech Computer Science")
