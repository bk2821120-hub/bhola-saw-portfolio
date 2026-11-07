from django.contrib import admin
from .models import Education

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_year', 'end_year', 'result', 'display_order', 'active']
    list_editable = ['display_order', 'active']
    search_fields = ['degree', 'institution']
