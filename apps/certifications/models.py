"""
Certifications app models
"""
from django.db import models


def cert_image_path(instance, filename):
    return f'certificates/{filename}'


def cert_pdf_path(instance, filename):
    return f'certificates/{filename}'


class Certification(models.Model):
    name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    issue_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to=cert_image_path, blank=True, null=True)
    pdf = models.FileField(upload_to=cert_pdf_path, blank=True, null=True)
    verification_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', '-issue_date']
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'

    def __str__(self):
        return f"{self.name} â€” {self.organization}"
