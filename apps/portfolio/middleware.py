"""
Middleware for handling site maintenance mode.
"""
from django.shortcuts import render
from apps.portfolio.models import WebsiteSetting


class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        if (
            path.startswith('/portal/')
            or path.startswith('/django-admin/')
            or path.startswith('/static/')
            or path.startswith('/media/')
            or path == '/favicon.ico'
        ):
            return self.get_response(request)

        if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
            return self.get_response(request)

        settings = WebsiteSetting.get_settings()
        if settings and settings.maintenance_mode:
            return render(request, 'public/maintenance.html', {'site_settings': settings}, status=503)

        return self.get_response(request)
