from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Service
from .forms import ServiceForm


@login_required
def service_list(request):
    services = Service.objects.all().order_by('display_order', 'title')
    return render(request, 'admin_panel/services/list.html', {
        'services': services,
        'page_title': 'Freelance Services'
    })


@login_required
def service_add(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service added successfully.')
            return redirect('services:list')
    else:
        form = ServiceForm()
    return render(request, 'admin_panel/services/form.html', {
        'form': form,
        'page_title': 'Add Service'
    })


@login_required
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service updated successfully.')
            return redirect('services:list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'admin_panel/services/form.html', {
        'form': form,
        'service': service,
        'page_title': 'Edit Service'
    })


@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Service deleted successfully.')
        return redirect('services:list')
    return render(request, 'admin_panel/services/delete.html', {
        'item': service,
        'page_title': 'Delete Service'
    })


@login_required
def service_toggle(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service.is_active = not service.is_active
    service.save()
    status = 'active' if service.is_active else 'hidden'
    messages.success(request, f'Service "{service.title}" is now {status}.')
    return redirect('services:list')
