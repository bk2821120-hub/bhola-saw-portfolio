from django.urls import path
from . import public_views

app_name = 'public'

urlpatterns = [
    path('', public_views.home, name='home'),
    path('about/', public_views.about, name='about'),
    path('skills/', public_views.skills, name='skills'),
    path('projects/', public_views.projects, name='projects'),
    path('projects/<slug:slug>/', public_views.project_detail, name='project_detail'),
    path('services/', public_views.services, name='services'),
    path('experience/', public_views.experience, name='experience'),
    path('education/', public_views.education, name='education'),
    path('certifications/', public_views.certifications, name='certifications'),
    path('achievements/', public_views.achievements, name='achievements'),
    path('blog/', public_views.blog_list, name='blog'),
    path('blog/<slug:slug>/', public_views.blog_detail, name='blog_detail'),
    path('resume/', public_views.resume, name='resume'),
    path('contact/', public_views.contact, name='contact'),
]
