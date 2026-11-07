from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    path('skills/', views.skill_list, name='list'),
    path('skills/add/', views.skill_add, name='add'),
    path('skills/<int:pk>/edit/', views.skill_edit, name='edit'),
    path('skills/<int:pk>/delete/', views.skill_delete, name='delete'),
    path('skills/<int:pk>/toggle/', views.skill_toggle, name='toggle'),
]
