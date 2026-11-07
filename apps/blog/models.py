"""
Blog app models: BlogTag, BlogPost
"""
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


def blog_thumbnail_path(instance, filename):
    return f'blog/{filename}'


class BlogTag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Blog Tag'
        verbose_name_plural = 'Blog Tags'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name) or 'tag'
            slug = base_slug
            counter = 1
            while BlogTag.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=320, unique=True, blank=True)
    thumbnail = models.ImageField(upload_to=blog_thumbnail_path, blank=True, null=True)
    content = models.TextField()
    tags = models.ManyToManyField(BlogTag, blank=True, related_name='posts')
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='blog_posts'
    )
    published = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or 'post'
            slug = base_slug
            counter = 1
            while BlogPost.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
