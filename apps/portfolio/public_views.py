"""
Public portfolio views â€” served at / (root URL).
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.portfolio.models import Profile, WebsiteSetting, SocialLink
from apps.projects.models import Project
from apps.skills.models import Skill, SkillCategory
from apps.education.models import Education
from apps.experience.models import Experience
from apps.certifications.models import Certification
from apps.achievements.models import Achievement
from apps.blog.models import BlogPost
from apps.documents.models import Document
from apps.contact.models import ContactMessage
from apps.contact.forms import ContactForm


def home(request):
    profile = Profile.get_active()
    featured_projects = Project.objects.filter(active=True, featured=True).prefetch_related('technologies').order_by('display_order')[:6]
    skills = Skill.objects.filter(active=True).select_related('category')
    recent_blog = BlogPost.objects.filter(published=True).order_by('-published_at', '-created_at')[:3]

    stats = {
        'projects': Project.objects.filter(active=True).count(),
        'skills': Skill.objects.filter(active=True).count(),
        'certifications': Certification.objects.filter(active=True).count(),
        'experience': Experience.objects.filter(active=True).count(),
    }

    return render(request, 'public/home.html', {
        'profile': profile,
        'featured_projects': featured_projects,
        'skills': skills,
        'recent_blog': recent_blog,
        'stats': stats,
    })


def about(request):
    profile = Profile.get_active()
    stats = {
        'projects': Project.objects.filter(active=True).count(),
        'skills': Skill.objects.filter(active=True).count(),
        'certifications': Certification.objects.filter(active=True).count(),
        'experience': Experience.objects.filter(active=True).count(),
    }
    return render(request, 'public/about.html', {'profile': profile, 'stats': stats})


def skills(request):
    categories = SkillCategory.objects.filter(active=True).prefetch_related(
        'skills'
    ).order_by('display_order')
    # Only include categories that have active skills
    categories_with_skills = [
        (cat, cat.skills.filter(active=True).order_by('display_order'))
        for cat in categories
        if cat.skills.filter(active=True).exists()
    ]
    return render(request, 'public/skills.html', {
        'categories_with_skills': categories_with_skills,
    })


def projects(request):
    category_filter = request.GET.get('category', '')
    all_projects = Project.objects.filter(active=True).prefetch_related('technologies').order_by('display_order', '-created_at')
    if category_filter:
        all_projects = all_projects.filter(category=category_filter)

    category_choices = Project.CATEGORY_CHOICES
    return render(request, 'public/projects.html', {
        'projects': all_projects,
        'category_choices': category_choices,
        'active_filter': category_filter,
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, active=True)
    related = Project.objects.filter(
        active=True, category=project.category
    ).exclude(pk=project.pk)[:3]
    return render(request, 'public/project_detail.html', {
        'project': project,
        'related_projects': related,
    })


def experience(request):
    experiences = Experience.objects.filter(active=True).order_by('display_order', '-start_date')
    return render(request, 'public/experience.html', {'experiences': experiences})


def education(request):
    educations = Education.objects.filter(active=True).order_by('display_order', '-start_year')
    return render(request, 'public/education.html', {'educations': educations})


def certifications(request):
    certs = Certification.objects.filter(active=True).order_by('display_order', '-issue_date')
    return render(request, 'public/certifications.html', {'certifications': certs})


def achievements(request):
    achievs = Achievement.objects.filter(active=True).order_by('display_order', '-date')
    return render(request, 'public/achievements.html', {'achievements': achievs})


def blog_list(request):
    posts = BlogPost.objects.filter(published=True).order_by('-published_at', '-created_at')
    return render(request, 'public/blog.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    related = BlogPost.objects.filter(published=True).exclude(pk=post.pk).order_by('-created_at')[:3]
    return render(request, 'public/blog_detail.html', {
        'post': post,
        'related_posts': related,
    })


def resume(request):
    active_resume = Document.objects.filter(
        document_type='resume', active=True, public=True
    ).first()
    return render(request, 'public/resume.html', {'resume': active_resume})


def services(request):
    from apps.services.models import Service
    services_list = Service.objects.filter(is_active=True).order_by('display_order', 'title')
    return render(request, 'public/services.html', {
        'services': services_list,
    })


def contact(request):
    initial_data = {}
    service_param = request.GET.get('service', '').strip()
    if service_param:
        from apps.services.models import Service
        matched = (
            Service.objects.filter(slug__iexact=service_param).first()
            or Service.objects.filter(title__iexact=service_param).first()
        )
        if matched:
            initial_data['service'] = matched.title
            initial_data['subject'] = f"Project Inquiry: {matched.title}"
        else:
            initial_data['service'] = service_param
            initial_data['subject'] = f"Project Inquiry: {service_param}"

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your project inquiry has been sent successfully. I will get back to you shortly.')
            return redirect('public:contact')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = ContactForm(initial=initial_data)

    return render(request, 'public/contact.html', {
        'form': form,
        'selected_service': initial_data.get('service', ''),
    })
