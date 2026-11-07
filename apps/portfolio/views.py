"""
Portfolio app â€” Admin portal views (Profile, WebsiteSetting, SocialLink)
and public views (home, about, contact).
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, WebsiteSetting, SocialLink
from .forms import ProfileForm, WebsiteSettingForm, SocialLinkForm


# â”€â”€â”€ Admin: Profile â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

@login_required
def admin_profile(request):
    profile = Profile.get_active()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('portfolio_admin:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'admin_panel/profile/form.html', {
        'form': form, 'page_title': 'Profile', 'profile': profile
    })


# â”€â”€â”€ Admin: Website Settings â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

@login_required
def admin_settings(request):
    setting = WebsiteSetting.get_settings()
    if request.method == 'POST':
        form = WebsiteSettingForm(request.POST, request.FILES, instance=setting)
        if form.is_valid():
            form.save()
            messages.success(request, 'Settings updated successfully.')
            return redirect('portfolio_admin:settings')
    else:
        form = WebsiteSettingForm(instance=setting)
    return render(request, 'admin_panel/settings/form.html', {
        'form': form, 'page_title': 'Website Settings'
    })


# â”€â”€â”€ Admin: Social Links â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

@login_required
def admin_social_links(request):
    links = SocialLink.objects.all()
    return render(request, 'admin_panel/social_links/list.html', {
        'links': links, 'page_title': 'Social Links'
    })


@login_required
def admin_social_link_add(request):
    if request.method == 'POST':
        form = SocialLinkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Social link added.')
            return redirect('portfolio_admin:social_links')
    else:
        form = SocialLinkForm()
    return render(request, 'admin_panel/social_links/form.html', {
        'form': form, 'page_title': 'Add Social Link'
    })


@login_required
def admin_social_link_edit(request, pk):
    link = get_object_or_404(SocialLink, pk=pk)
    if request.method == 'POST':
        form = SocialLinkForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            messages.success(request, 'Social link updated.')
            return redirect('portfolio_admin:social_links')
    else:
        form = SocialLinkForm(instance=link)
    return render(request, 'admin_panel/social_links/form.html', {
        'form': form, 'page_title': 'Edit Social Link', 'link': link
    })


@login_required
def admin_social_link_delete(request, pk):
    link = get_object_or_404(SocialLink, pk=pk)
    if request.method == 'POST':
        link.delete()
        messages.success(request, 'Social link deleted.')
        return redirect('portfolio_admin:social_links')
    return render(request, 'admin_panel/social_links/delete.html', {
        'link': link, 'page_title': 'Delete Social Link'
    })
