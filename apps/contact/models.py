"""
Contact app models
"""
from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    service = models.CharField(max_length=200, blank=True, help_text='Service inquired about')
    budget = models.CharField(max_length=100, blank=True, help_text='Project budget')
    timeline = models.CharField(max_length=100, blank=True, help_text='Expected timeline')
    subject = models.CharField(max_length=300, blank=True)
    message = models.TextField(help_text='Project description / requirements')
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        subj = self.subject or self.service or "Inquiry"
        return f"{self.name} — {subj}"
