from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from apps.contact.models import ContactMessage


class ContactTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="admin", password="password123")

    def test_contact_form_valid_submission(self):
        resp = self.client.post(reverse('public:contact'), {
            'name': 'Visitor',
            'email': 'visitor@example.com',
            'subject': 'Inquiry',
            'message': 'Hello from contact test.'
        }, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(ContactMessage.objects.filter(email='visitor@example.com').exists())

    def test_contact_form_invalid_email(self):
        resp = self.client.post(reverse('public:contact'), {
            'name': 'Visitor',
            'email': 'invalid-email',
            'subject': 'Inquiry',
            'message': 'Hello'
        })
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(ContactMessage.objects.filter(name='Visitor').exists())

    def test_message_detail_marks_as_read(self):
        msg = ContactMessage.objects.create(
            name="Alice",
            email="alice@example.com",
            subject="Test Msg",
            message="Message content",
            read=False
        )
        self.client.force_login(self.user)
        resp = self.client.get(reverse('contact:message_detail', kwargs={'pk': msg.pk}))
        self.assertEqual(resp.status_code, 200)
        msg.refresh_from_db()
        self.assertTrue(msg.read)
