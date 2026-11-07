from django.urls import path
from . import views

app_name = 'achievements'

urlpatterns = [
    path('achievements/', views.achievement_list, name='list'),
    path('achievements/add/', views.achievement_add, name='add'),
    path('achievements/<int:pk>/edit/', views.achievement_edit, name='edit'),
    path('achievements/<int:pk>/delete/', views.achievement_delete, name='delete'),
]
