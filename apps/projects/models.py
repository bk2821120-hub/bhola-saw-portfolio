"""
Projects app models: Project, ProjectTechnology
"""
from django.db import models
from django.utils.text import slugify


def project_image_path(instance, filename):
    return f'projects/{filename}'


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('machine_learning', 'Machine Learning'),
        ('nlp', 'NLP'),
        ('deep_learning', 'Deep Learning'),
        ('computer_vision', 'Computer Vision'),
        ('web_development', 'Web Development'),
        ('data_analytics', 'Data Analytics'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('planned', 'Planned'),
        ('on_hold', 'On Hold'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    thumbnail = models.ImageField(upload_to=project_image_path, blank=True, null=True)
    short_description = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    problem_statement = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    featured = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    github_url = models.URLField(blank=True)
    live_demo_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or 'project'
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class ProjectTechnology(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='technologies')
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Project Technology'
        verbose_name_plural = 'Project Technologies'

    def __str__(self):
        return f"{self.project.title} â€” {self.name}"
