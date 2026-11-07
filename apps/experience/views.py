from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Experience
from .forms import ExperienceForm

@login_required
def experience_list(request):
    items = Experience.objects.all().order_by('display_order', '-start_date')
    return render(request, 'admin_panel/experience/list.html', {'items': items, 'page_title': 'Experience'})

@login_required
def experience_add(request):
    form = ExperienceForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Experience added.')
        return redirect('experience:list')
    return render(request, 'admin_panel/experience/form.html', {'form': form, 'page_title': 'Add Experience'})

@login_required
def experience_edit(request, pk):
    item = get_object_or_404(Experience, pk=pk)
    form = ExperienceForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, 'Experience updated.')
        return redirect('experience:list')
    return render(request, 'admin_panel/experience/form.html', {'form': form, 'item': item, 'page_title': 'Edit Experience'})

@login_required
def experience_delete(request, pk):
    item = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Experience deleted.')
        return redirect('experience:list')
    return render(request, 'admin_panel/experience/delete.html', {'item': item, 'page_title': 'Delete Experience'})
