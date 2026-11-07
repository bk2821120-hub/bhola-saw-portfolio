from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'read', 'created_at']
    list_editable = ['read']
    list_filter = ['read']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
