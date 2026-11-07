from django.urls import path
from . import views

app_name = 'certifications'

urlpatterns = [
    path('certifications/', views.cert_list, name='list'),
    path('certifications/add/', views.cert_add, name='add'),
    path('certifications/<int:pk>/edit/', views.cert_edit, name='edit'),
    path('certifications/<int:pk>/delete/', views.cert_delete, name='delete'),
    path('certifications/<int:pk>/toggle/', views.cert_toggle, name='toggle'),
]
