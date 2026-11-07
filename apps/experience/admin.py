from django.contrib import admin
from .models import Experience

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'employment_type', 'start_date', 'currently_working', 'display_order', 'active']
    list_editable = ['display_order', 'active']
    list_filter = ['employment_type', 'currently_working', 'active']
    search_fields = ['company', 'position']
