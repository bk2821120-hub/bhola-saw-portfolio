from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Document
from .forms import DocumentForm

@login_required
def document_list(request):
    docs = Document.objects.all().order_by('-uploaded_at')
    return render(request, 'admin_panel/documents/list.html', {'docs': docs, 'page_title': 'Documents'})

@login_required
def document_upload(request):
    form = DocumentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Document uploaded.')
        return redirect('documents:list')
    return render(request, 'admin_panel/documents/upload.html', {'form': form, 'page_title': 'Upload Document'})

@login_required
def document_edit(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    form = DocumentForm(request.POST or None, request.FILES or None, instance=doc)
    if form.is_valid():
        form.save()
        messages.success(request, 'Document updated.')
        return redirect('documents:list')
    return render(request, 'admin_panel/documents/upload.html', {'form': form, 'doc': doc, 'page_title': 'Edit Document'})

@login_required
def document_delete(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        doc.delete()
        messages.success(request, 'Document deleted.')
        return redirect('documents:list')
    return render(request, 'admin_panel/documents/delete.html', {'doc': doc, 'page_title': 'Delete Document'})

@login_required
def document_set_active(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    doc.active = not doc.active
    doc.save()
    status = "active" if doc.active else "inactive"
    messages.success(request, f'"{doc.name}" is now {status}.')
    return redirect('documents:list')
