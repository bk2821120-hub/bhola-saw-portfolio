from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['name', 'document_type', 'active', 'public', 'uploaded_at']
    list_editable = ['active', 'public']
    list_filter = ['document_type', 'active', 'public']
    search_fields = ['name']
