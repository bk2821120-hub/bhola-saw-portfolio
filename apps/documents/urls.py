from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    path('documents/', views.document_list, name='list'),
    path('documents/upload/', views.document_upload, name='upload'),
    path('documents/<int:pk>/edit/', views.document_edit, name='edit'),
    path('documents/<int:pk>/delete/', views.document_delete, name='delete'),
    path('documents/<int:pk>/set-active/', views.document_set_active, name='set_active'),
]
