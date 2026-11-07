from django.contrib import admin
from .models import Project, ProjectTechnology

class ProjectTechnologyInline(admin.TabularInline):
    model = ProjectTechnology
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'featured', 'display_order', 'active']
    list_editable = ['featured', 'display_order', 'active']
    list_filter = ['category', 'status', 'featured', 'active']
    search_fields = ['title', 'short_description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectTechnologyInline]
