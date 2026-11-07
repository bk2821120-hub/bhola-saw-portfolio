from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.blog_list, name='list'),
    path('blog/add/', views.blog_add, name='add'),
    path('blog/<int:pk>/edit/', views.blog_edit, name='edit'),
    path('blog/<int:pk>/delete/', views.blog_delete, name='delete'),
    path('blog/<int:pk>/toggle/', views.blog_toggle_publish, name='toggle'),
]
