"""
Admin portal views for Projects CRUD.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, ProjectTechnology
from .forms import ProjectForm


@login_required
def project_list(request):
    projects = Project.objects.prefetch_related('technologies').order_by('display_order', '-created_at')
    return render(request, 'admin_panel/projects/list.html', {
        'projects': projects, 'page_title': 'Projects'
    })


@login_required
def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            _save_technologies(project, form.cleaned_data.get('technologies', ''))
            messages.success(request, 'Project added successfully.')
            return redirect('projects:list')
    else:
        form = ProjectForm()
    return render(request, 'admin_panel/projects/form.html', {
        'form': form, 'page_title': 'Add Project'
    })


@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            _save_technologies(project, form.cleaned_data.get('technologies', ''))
            messages.success(request, 'Project updated successfully.')
            return redirect('projects:list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'admin_panel/projects/form.html', {
        'form': form, 'project': project, 'page_title': 'Edit Project'
    })


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted.')
        return redirect('projects:list')
    return render(request, 'admin_panel/projects/delete.html', {
        'project': project, 'page_title': 'Delete Project'
    })


@login_required
def project_toggle(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.active = not project.active
    project.save()
    messages.success(request, f'Project "{project.title}" is now {"active" if project.active else "inactive"}.')
    return redirect('projects:list')


def _save_technologies(project, tech_string):
    """Parse comma-separated tech string and save to ProjectTechnology."""
    project.technologies.all().delete()
    if tech_string:
        for tech in tech_string.split(','):
            tech = tech.strip()
            if tech:
                ProjectTechnology.objects.create(project=project, name=tech)
