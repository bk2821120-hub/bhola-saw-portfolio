from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Achievement
from .forms import AchievementForm

@login_required
def achievement_list(request):
    items = Achievement.objects.all().order_by('display_order', '-date')
    return render(request, 'admin_panel/achievements/list.html', {'items': items, 'page_title': 'Achievements'})

@login_required
def achievement_add(request):
    form = AchievementForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Achievement added.')
        return redirect('achievements:list')
    return render(request, 'admin_panel/achievements/form.html', {'form': form, 'page_title': 'Add Achievement'})

@login_required
def achievement_edit(request, pk):
    item = get_object_or_404(Achievement, pk=pk)
    form = AchievementForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, 'Achievement updated.')
        return redirect('achievements:list')
    return render(request, 'admin_panel/achievements/form.html', {'form': form, 'item': item, 'page_title': 'Edit Achievement'})

@login_required
def achievement_delete(request, pk):
    item = get_object_or_404(Achievement, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Achievement deleted.')
        return redirect('achievements:list')
    return render(request, 'admin_panel/achievements/delete.html', {'item': item, 'page_title': 'Delete Achievement'})
