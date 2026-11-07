from django.contrib import admin
from .models import Profile, WebsiteSetting, SocialLink


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'professional_title', 'email', 'updated_at']
    search_fields = ['name', 'email']


@admin.register(WebsiteSetting)
class WebsiteSettingAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'maintenance_mode', 'updated_at']


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'display_order', 'active']
    list_editable = ['display_order', 'active']
    list_filter = ['active', 'platform']
