from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'starting_price', 'display_order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'short_description', 'description', 'technologies')
    list_editable = ('display_order', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
