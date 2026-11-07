from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('services/', views.service_list, name='list'),
    path('services/add/', views.service_add, name='add'),
    path('services/<int:pk>/edit/', views.service_edit, name='edit'),
    path('services/<int:pk>/delete/', views.service_delete, name='delete'),
    path('services/<int:pk>/toggle/', views.service_toggle, name='toggle'),
]
