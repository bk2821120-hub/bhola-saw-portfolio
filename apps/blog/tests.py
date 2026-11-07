from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from apps.blog.models import BlogPost, BlogTag


class BlogTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="author", password="password123")
        self.post = BlogPost.objects.create(
            title="Django Performance Tips",
            content="Use select_related and prefetch_related for optimal queries.",
            author=self.user,
            published=True,
            published_at=timezone.now()
        )

    def test_unique_slug_and_collision(self):
        self.assertEqual(self.post.slug, "django-performance-tips")
        dup = BlogPost.objects.create(
            title="Django Performance Tips",
            content="Duplicate article"
        )
        self.assertEqual(dup.slug, "django-performance-tips-1")

    def test_public_blog_views(self):
        # List
        resp_list = self.client.get(reverse('public:blog'))
        self.assertEqual(resp_list.status_code, 200)
        self.assertContains(resp_list, "Django Performance Tips")

        # Detail
        resp_detail = self.client.get(reverse('public:blog_detail', kwargs={'slug': self.post.slug}))
        self.assertEqual(resp_detail.status_code, 200)
        self.assertContains(resp_detail, "Django Performance Tips")

    def test_blog_toggle_publish(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('blog:toggle', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 302)
        self.post.refresh_from_db()
        self.assertFalse(self.post.published)
