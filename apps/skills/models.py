"""
Skills app models: SkillCategory, Skill
"""
from django.db import models
from django.utils.text import slugify


class SkillCategory(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming'),
        ('data_analytics', 'Data & Analytics'),
        ('machine_learning', 'Machine Learning'),
        ('nlp', 'NLP'),
        ('deep_learning', 'Deep Learning'),
        ('web_development', 'Web Development'),
        ('database', 'Database'),
        ('tools', 'Tools'),
        ('cloud', 'Cloud'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'name']
        verbose_name = 'Skill Category'
        verbose_name_plural = 'Skill Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name) or 'category'
            slug = base_slug
            counter = 1
            while SkillCategory.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Skill(models.Model):
    LEVEL_CHOICES = [
        (1, 'Beginner'),
        (2, 'Elementary'),
        (3, 'Intermediate'),
        (4, 'Advanced'),
        (5, 'Expert'),
    ]
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        SkillCategory, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='skills'
    )
    description = models.TextField(blank=True)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES, default=3)
    icon = models.CharField(max_length=100, blank=True, help_text='Bootstrap icon class or image path')
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'name']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

    @property
    def level_percentage(self):
        return self.level * 20
