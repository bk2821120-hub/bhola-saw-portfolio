"""
Global template context processor â€” injects site settings, profile, and social links
into every template automatically.
"""
from .models import Profile, WebsiteSetting, SocialLink


def global_context(request):
    profile = Profile.get_active()
    settings = WebsiteSetting.get_settings()
    social_links = SocialLink.objects.filter(active=True)
    return {
        'profile': profile,
        'site_settings': settings,
        'social_links': social_links,
    }
