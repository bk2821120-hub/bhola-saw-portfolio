"""
Admin portal views for Skills and SkillCategories CRUD.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Skill, SkillCategory
from .forms import SkillForm, SkillCategoryForm


@login_required
def skill_list(request):
    skills = Skill.objects.select_related('category').order_by('display_order', 'name')
    categories = SkillCategory.objects.filter(active=True)
    return render(request, 'admin_panel/skills/list.html', {
        'skills': skills, 'categories': categories, 'page_title': 'Skills'
    })


@login_required
def skill_add(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill added successfully.')
            return redirect('skills:list')
    else:
        form = SkillForm()
    return render(request, 'admin_panel/skills/form.html', {
        'form': form, 'page_title': 'Add Skill'
    })


@login_required
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully.')
            return redirect('skills:list')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'admin_panel/skills/form.html', {
        'form': form, 'skill': skill, 'page_title': 'Edit Skill'
    })


@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted.')
        return redirect('skills:list')
    return render(request, 'admin_panel/skills/delete.html', {
        'skill': skill, 'page_title': 'Delete Skill'
    })


@login_required
def skill_toggle(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.active = not skill.active
    skill.save()
    status = 'shown' if skill.active else 'hidden'
    messages.success(request, f'Skill "{skill.name}" is now {status}.')
    return redirect('skills:list')
