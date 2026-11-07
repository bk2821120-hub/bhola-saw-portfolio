"""
Education app models
"""
from django.db import models


def institution_logo_path(instance, filename):
    return f'education/{filename}'


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    university_or_board = models.CharField(max_length=200, blank=True)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(blank=True, null=True)
    result = models.CharField(max_length=100, blank=True, help_text='CGPA, Percentage, Grade, etc.')
    description = models.TextField(blank=True)
    institution_logo = models.ImageField(upload_to=institution_logo_path, blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', '-start_year']
        verbose_name = 'Education'
        verbose_name_plural = 'Education Records'

    def __str__(self):
        return f"{self.degree} â€” {self.institution}"

    @property
    def duration(self):
        end = self.end_year or 'Present'
        return f"{self.start_year} â€” {end}"
