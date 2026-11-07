from django.contrib import admin
from .models import Achievement

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'date', 'display_order', 'active']
    list_editable = ['display_order', 'active']
    search_fields = ['title', 'organization']
