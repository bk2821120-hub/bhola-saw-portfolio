from django.urls import path
from . import views

app_name = 'experience'

urlpatterns = [
    path('experience/', views.experience_list, name='list'),
    path('experience/add/', views.experience_add, name='add'),
    path('experience/<int:pk>/edit/', views.experience_edit, name='edit'),
    path('experience/<int:pk>/delete/', views.experience_delete, name='delete'),
]
