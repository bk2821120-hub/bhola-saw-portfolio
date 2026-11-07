from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    short_description = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    deliverables = models.TextField(
        blank=True,
        help_text="Deliverables and key outputs (one per line)"
    )
    technologies = models.CharField(
        max_length=300,
        blank=True,
        help_text="Comma-separated technologies (e.g. Python, Pandas, Matplotlib)"
    )
    icon = models.CharField(
        max_length=100,
        default="bi-gear",
        help_text="Bootstrap icon class, e.g. bi-file-earmark-spreadsheet"
    )
    starting_price = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional starting price or quote (e.g. '$49' or 'Custom Quote')"
    )
    is_active = models.BooleanField(default=True, verbose_name="Active")
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'title']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title

    @property
    def deliverables_list(self):
        return [d.strip() for d in self.deliverables.splitlines() if d.strip()]

    @property
    def technologies_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or 'service'
            slug = base_slug
            counter = 1
            while Service.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
