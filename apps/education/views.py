from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Education
from .forms import EducationForm

@login_required
def education_list(request):
    items = Education.objects.all().order_by('display_order', '-start_year')
    return render(request, 'admin_panel/education/list.html', {'items': items, 'page_title': 'Education'})

@login_required
def education_add(request):
    form = EducationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Education record added.')
        return redirect('education:list')
    return render(request, 'admin_panel/education/form.html', {'form': form, 'page_title': 'Add Education'})

@login_required
def education_edit(request, pk):
    item = get_object_or_404(Education, pk=pk)
    form = EducationForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, 'Education record updated.')
        return redirect('education:list')
    return render(request, 'admin_panel/education/form.html', {'form': form, 'item': item, 'page_title': 'Edit Education'})

@login_required
def education_delete(request, pk):
    item = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Education record deleted.')
        return redirect('education:list')
    return render(request, 'admin_panel/education/delete.html', {'item': item, 'page_title': 'Delete Education'})
