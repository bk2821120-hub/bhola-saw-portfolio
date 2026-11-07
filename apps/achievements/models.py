"""
Achievements app models
"""
from django.db import models


def achievement_image_path(instance, filename):
    return f'achievements/{filename}'


def achievement_pdf_path(instance, filename):
    return f'achievements/{filename}'


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200, blank=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=achievement_image_path, blank=True, null=True)
    pdf = models.FileField(upload_to=achievement_pdf_path, blank=True, null=True)
    verification_url = models.URLField(blank=True)
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', '-date']
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'

    def __str__(self):
        return self.title
