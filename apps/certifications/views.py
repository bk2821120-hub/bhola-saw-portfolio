from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Certification
from .forms import CertificationForm

@login_required
def cert_list(request):
    items = Certification.objects.all().order_by('display_order', '-issue_date')
    return render(request, 'admin_panel/certifications/list.html', {'items': items, 'page_title': 'Certifications'})

@login_required
def cert_add(request):
    form = CertificationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Certification added.')
        return redirect('certifications:list')
    return render(request, 'admin_panel/certifications/form.html', {'form': form, 'page_title': 'Add Certification'})

@login_required
def cert_edit(request, pk):
    item = get_object_or_404(Certification, pk=pk)
    form = CertificationForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, 'Certification updated.')
        return redirect('certifications:list')
    return render(request, 'admin_panel/certifications/form.html', {'form': form, 'item': item, 'page_title': 'Edit Certification'})

@login_required
def cert_delete(request, pk):
    item = get_object_or_404(Certification, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Certification deleted.')
        return redirect('certifications:list')
    return render(request, 'admin_panel/certifications/delete.html', {'item': item, 'page_title': 'Delete Certification'})

@login_required
def cert_toggle(request, pk):
    item = get_object_or_404(Certification, pk=pk)
    item.active = not item.active
    item.save()
    messages.success(request, f'Certification is now {"active" if item.active else "inactive"}.')
    return redirect('certifications:list')
