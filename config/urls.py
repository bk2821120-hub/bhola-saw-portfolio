"""
Root URL configuration for Portfolio CMS.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

# Rename Django's default admin site
admin.site.site_header = "Portfolio CMS — Super Admin"
admin.site.site_title = "Portfolio Super Admin"
admin.site.index_title = "Administration"

urlpatterns = [
    # Favicon redirect
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.png', permanent=True)),

    # Django built-in admin
    path('django-admin/', admin.site.urls),

    # Custom admin/portal
    path('portal/', include('apps.accounts.urls', namespace='accounts')),
    path('portal/', include('apps.portfolio.urls', namespace='portfolio_admin')),
    path('portal/', include('apps.projects.urls', namespace='projects')),
    path('portal/', include('apps.services.urls', namespace='services')),
    path('portal/', include('apps.skills.urls', namespace='skills')),
    path('portal/', include('apps.education.urls', namespace='education')),
    path('portal/', include('apps.experience.urls', namespace='experience')),
    path('portal/', include('apps.certifications.urls', namespace='certifications')),
    path('portal/', include('apps.achievements.urls', namespace='achievements')),
    path('portal/', include('apps.blog.urls', namespace='blog')),
    path('portal/', include('apps.documents.urls', namespace='documents')),
    path('portal/', include('apps.contact.urls', namespace='contact')),

    # Public website (must be last)
    path('', include('apps.portfolio.public_urls', namespace='public')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
