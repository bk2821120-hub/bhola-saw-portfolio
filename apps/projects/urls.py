from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('projects/', views.project_list, name='list'),
    path('projects/add/', views.project_add, name='add'),
    path('projects/<int:pk>/edit/', views.project_edit, name='edit'),
    path('projects/<int:pk>/delete/', views.project_delete, name='delete'),
    path('projects/<int:pk>/toggle/', views.project_toggle, name='toggle'),
]
