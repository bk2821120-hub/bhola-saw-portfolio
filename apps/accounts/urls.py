from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.portal_login, name='login'),
    path('logout/', views.portal_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
