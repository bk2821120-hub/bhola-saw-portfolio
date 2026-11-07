"""
Experience app models
"""
from django.db import models


def company_logo_path(instance, filename):
    return f'experience/{filename}'


class Experience(models.Model):
    EMPLOYMENT_TYPE_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
        ('contract', 'Contract'),
        ('volunteer', 'Volunteer'),
    ]

    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES, default='full_time')
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_working = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    responsibilities = models.TextField(blank=True, help_text='One responsibility per line')
    skills_used = models.CharField(max_length=500, blank=True, help_text='Comma-separated skills')
    company_logo = models.ImageField(upload_to=company_logo_path, blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', '-start_date']
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return f"{self.position} at {self.company}"

    @property
    def end_display(self):
        if self.currently_working:
            return 'Present'
        return self.end_date.strftime('%b %Y') if self.end_date else 'Present'

    @property
    def responsibilities_list(self):
        return [r.strip() for r in self.responsibilities.splitlines() if r.strip()]

    @property
    def skills_list(self):
        return [s.strip() for s in self.skills_used.split(',') if s.strip()]
