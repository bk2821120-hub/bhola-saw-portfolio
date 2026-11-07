from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.documents.models import Document


class DocumentsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="admin", password="password123")
        dummy_file = SimpleUploadedFile("resume.pdf", b"%PDF-1.4 dummy pdf content", content_type="application/pdf")
        self.doc1 = Document.objects.create(
            name="Resume 2025",
            document_type="resume",
            file=dummy_file,
            active=True,
            public=True
        )

    def test_resume_deactivates_older_resumes(self):
        dummy_file2 = SimpleUploadedFile("resume2.pdf", b"%PDF-1.4 dummy pdf content 2", content_type="application/pdf")
        doc2 = Document.objects.create(
            name="Resume 2026",
            document_type="resume",
            file=dummy_file2,
            active=True,
            public=True
        )
        self.doc1.refresh_from_db()
        self.assertFalse(self.doc1.active)
        self.assertTrue(doc2.active)

    def test_public_resume_page(self):
        resp = self.client.get(reverse('public:resume'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Resume 2025")

    def test_admin_document_toggle_active(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('documents:set_active', kwargs={'pk': self.doc1.pk}))
        self.assertEqual(resp.status_code, 302)
        self.doc1.refresh_from_db()
        self.assertFalse(self.doc1.active)
