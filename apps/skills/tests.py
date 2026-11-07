from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from apps.skills.models import Skill, SkillCategory


class SkillsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="admin", password="password123")
        self.category = SkillCategory.objects.create(name="Backend Development")
        self.skill = Skill.objects.create(
            name="Django",
            category=self.category,
            level=5,
            icon="bi-hdd-network",
            active=True
        )

    def test_skill_category_slug_collision(self):
        self.assertEqual(self.category.slug, "backend-development")
        dup = SkillCategory.objects.create(name="Backend Development")
        self.assertEqual(dup.slug, "backend-development-1")

    def test_skill_level_percentage(self):
        self.assertEqual(self.skill.level_percentage, 100)

    def test_public_skills_view(self):
        resp = self.client.get(reverse('public:skills'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Django")
        self.assertContains(resp, "Backend Development")

    def test_skill_toggle(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('skills:toggle', kwargs={'pk': self.skill.pk}))
        self.assertEqual(resp.status_code, 302)
        self.skill.refresh_from_db()
        self.assertFalse(self.skill.active)
