import datetime
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from apps.projects.models import Project, ProjectTechnology
from apps.projects.forms import ProjectForm


class ProjectsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testadmin", password="password123")
        self.project = Project.objects.create(
            title="Django Web CMS",
            short_description="A dynamic CMS",
            description="Detailed description",
            category="web_development",
            status="completed",
            active=True
        )

    def test_unique_slug_generation_and_collision(self):
        self.assertEqual(self.project.slug, "django-web-cms")
        duplicate_project = Project.objects.create(
            title="Django Web CMS",
            short_description="Duplicate CMS"
        )
        self.assertEqual(duplicate_project.slug, "django-web-cms-1")

    def test_public_project_detail_view(self):
        resp = self.client.get(reverse('public:project_detail', kwargs={'slug': self.project.slug}))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Django Web CMS")

    def test_date_validation_in_project_form(self):
        form = ProjectForm(data={
            'title': 'Test Project',
            'category': 'web_development',
            'status': 'completed',
            'start_date': datetime.date(2025, 5, 1),
            'end_date': datetime.date(2024, 5, 1),  # earlier than start date
        })
        self.assertFalse(form.is_valid())
        self.assertIn('end_date', form.errors)

    def test_admin_project_crud(self):
        self.client.force_login(self.user)
        # List
        resp = self.client.get(reverse('projects:list'))
        self.assertEqual(resp.status_code, 200)

        # Toggle
        resp_toggle = self.client.get(reverse('projects:toggle', kwargs={'pk': self.project.pk}))
        self.assertEqual(resp_toggle.status_code, 302)
        self.project.refresh_from_db()
        self.assertFalse(self.project.active)
