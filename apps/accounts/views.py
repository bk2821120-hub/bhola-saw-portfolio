"""
Accounts views â€” custom portal login/logout.
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import PortalLoginForm


def portal_login(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')

    if request.method == 'POST':
        form = PortalLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', '')
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = PortalLoginForm()

    return render(request, 'admin_panel/login.html', {'form': form})


def portal_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('accounts:login')


@login_required
def dashboard(request):
    from apps.projects.models import Project
    from apps.services.models import Service
    from apps.skills.models import Skill
    from apps.certifications.models import Certification
    from apps.experience.models import Experience
    from apps.education.models import Education
    from apps.achievements.models import Achievement
    from apps.blog.models import BlogPost
    from apps.documents.models import Document
    from apps.contact.models import ContactMessage

    stats = {
        'projects': Project.objects.filter(active=True).count(),
        'services': Service.objects.filter(is_active=True).count(),
        'skills': Skill.objects.filter(active=True).count(),
        'certifications': Certification.objects.filter(active=True).count(),
        'experiences': Experience.objects.filter(active=True).count(),
        'educations': Education.objects.filter(active=True).count(),
        'achievements': Achievement.objects.filter(active=True).count(),
        'blog_posts': BlogPost.objects.filter(published=True).count(),
        'documents': Document.objects.count(),
        'unread_messages': ContactMessage.objects.filter(read=False).count(),
        'total_messages': ContactMessage.objects.count(),
    }
    recent_projects = Project.objects.filter(active=True).order_by('-created_at')[:5]
    recent_messages = ContactMessage.objects.order_by('-created_at')[:5]
    recent_certs = Certification.objects.filter(active=True).order_by('-created_at')[:5]
    recent_posts = BlogPost.objects.filter(published=True).order_by('-created_at')[:5]

    context = {
        'stats': stats,
        'recent_projects': recent_projects,
        'recent_messages': recent_messages,
        'recent_certs': recent_certs,
        'recent_posts': recent_posts,
        'page_title': 'Dashboard',
    }
    return render(request, 'admin_panel/dashboard.html', context)
