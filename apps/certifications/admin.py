from django.contrib import admin
from .models import Certification

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization', 'issue_date', 'display_order', 'active']
    list_editable = ['display_order', 'active']
    list_filter = ['active', 'organization']
    search_fields = ['name', 'organization', 'credential_id']
