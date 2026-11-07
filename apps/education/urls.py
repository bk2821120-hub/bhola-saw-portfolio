from django.urls import path
from . import views

app_name = 'education'

urlpatterns = [
    path('education/', views.education_list, name='list'),
    path('education/add/', views.education_add, name='add'),
    path('education/<int:pk>/edit/', views.education_edit, name='edit'),
    path('education/<int:pk>/delete/', views.education_delete, name='delete'),
]
