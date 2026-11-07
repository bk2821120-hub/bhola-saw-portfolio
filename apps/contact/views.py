from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactForm

@login_required
def message_list(request):
    msgs = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'admin_panel/messages/list.html', {'messages_list': msgs, 'page_title': 'Messages'})

@login_required
def message_detail(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    if not msg.read:
        msg.read = True
        msg.save()
    return render(request, 'admin_panel/messages/detail.html', {'msg': msg, 'page_title': 'Message Detail'})

@login_required
def message_toggle_read(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    msg.read = not msg.read
    msg.save()
    return redirect('contact:message_list')

@login_required
def message_delete(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    if request.method == 'POST':
        msg.delete()
        messages.success(request, 'Message deleted.')
        return redirect('contact:message_list')
    return render(request, 'admin_panel/messages/delete.html', {'msg': msg, 'page_title': 'Delete Message'})
