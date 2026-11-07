from django.contrib import admin
from .models import SkillCategory, Skill

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'display_order', 'active']
    list_editable = ['display_order', 'active']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'level', 'display_order', 'active']
    list_editable = ['display_order', 'active']
    list_filter = ['category', 'level', 'active']
    search_fields = ['name']
