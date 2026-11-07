from django.urls import path
from . import views

app_name = 'portfolio_admin'

urlpatterns = [
    path('profile/', views.admin_profile, name='profile'),
    path('settings/', views.admin_settings, name='settings'),
    path('social-links/', views.admin_social_links, name='social_links'),
    path('social-links/add/', views.admin_social_link_add, name='social_link_add'),
    path('social-links/<int:pk>/edit/', views.admin_social_link_edit, name='social_link_edit'),
    path('social-links/<int:pk>/delete/', views.admin_social_link_delete, name='social_link_delete'),
]
