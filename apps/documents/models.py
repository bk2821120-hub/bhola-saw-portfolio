"""
Documents app models
"""
from django.db import models


def document_upload_path(instance, filename):
    doc_type = instance.document_type.lower().replace(' ', '_')
    return f'documents/{doc_type}/{filename}'


class Document(models.Model):
    TYPE_CHOICES = [
        ('resume', 'Resume'),
        ('cv', 'CV'),
        ('certificate', 'Certificate'),
        ('project_report', 'Project Report'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    document_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='resume')
    file = models.FileField(upload_to=document_upload_path)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False, help_text='Set as active/current version')
    public = models.BooleanField(default=True, help_text='Visible to public visitors')

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return f"{self.name} ({self.get_document_type_display()})"

    def save(self, *args, **kwargs):
        # If this document is set active and is a resume, deactivate other resumes
        if self.active and self.document_type == 'resume':
            Document.objects.filter(
                document_type='resume', active=True
            ).exclude(pk=self.pk).update(active=False)
        super().save(*args, **kwargs)
