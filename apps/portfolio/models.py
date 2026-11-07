"""
Portfolio app models: Profile, WebsiteSetting, SocialLink
"""
from django.db import models


def profile_upload_path(instance, filename):
    return f'profile/{filename}'


def logo_upload_path(instance, filename):
    return f'settings/{filename}'


class Profile(models.Model):
    name = models.CharField(max_length=200)
    professional_title = models.CharField(max_length=200, blank=True)
    short_intro = models.CharField(max_length=500, blank=True)
    bio = models.TextField(blank=True)
    career_objective = models.TextField(blank=True)
    current_focus = models.CharField(max_length=300, blank=True)
    photo = models.ImageField(upload_to=profile_upload_path, blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=200, blank=True)
    resume_tagline = models.CharField(max_length=300, blank=True)
    years_of_experience = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @classmethod
    def get_active(cls):
        """Return the first (most recently created) profile."""
        return cls.objects.first()


class WebsiteSetting(models.Model):
    site_name = models.CharField(max_length=200, default='My Portfolio')
    logo = models.ImageField(upload_to=logo_upload_path, blank=True, null=True)
    favicon = models.ImageField(upload_to=logo_upload_path, blank=True, null=True)
    primary_color = models.CharField(max_length=10, default='#6366f1')
    secondary_color = models.CharField(max_length=10, default='#8b5cf6')
    seo_title = models.CharField(max_length=200, blank=True)
    seo_description = models.TextField(blank=True)
    footer_text = models.CharField(max_length=500, blank=True)
    maintenance_mode = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Website Setting'
        verbose_name_plural = 'Website Settings'

    def __str__(self):
        return self.site_name

    @classmethod
    def get_settings(cls):
        return cls.objects.first()


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('email', 'Email'),
        ('youtube', 'YouTube'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter / X'),
        ('facebook', 'Facebook'),
        ('kaggle', 'Kaggle'),
        ('other', 'Other'),
    ]
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField(max_length=500)
    icon = models.CharField(max_length=100, blank=True, help_text='Bootstrap icon class, e.g. bi-github')
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'platform']
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'

    def __str__(self):
        return f"{self.get_platform_display()} â€” {self.url}"
