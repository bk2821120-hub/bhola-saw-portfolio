from django import forms
from .models import Profile, WebsiteSetting, SocialLink


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'professional_title': forms.TextInput(attrs={'class': 'form-control'}),
            'short_intro': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'career_objective': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'current_focus': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'resume_tagline': forms.TextInput(attrs={'class': 'form-control'}),
            'years_of_experience': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class WebsiteSettingForm(forms.ModelForm):
    class Meta:
        model = WebsiteSetting
        fields = '__all__'
        widgets = {
            'site_name': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'favicon': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'primary_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'secondary_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'seo_title': forms.TextInput(attrs={'class': 'form-control'}),
            'seo_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'footer_text': forms.TextInput(attrs={'class': 'form-control'}),
            'maintenance_mode': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


import re

def clean_bootstrap_icon_class(val):
    if not val:
        return ''
    val = val.strip()
    # 1. Search for any bi-* class inside HTML or text
    m = re.search(r'\b(bi-[a-zA-Z0-9_-]+)\b', val)
    if m:
        return m.group(1)
    
    # 2. If entered without bi- prefix like 'linkedin' or 'github'
    tag_stripped = re.sub(r'[<>/]', '', val).strip()
    parts = tag_stripped.split()
    for p in parts:
        if p.startswith('bi-'):
            return p
        if p != 'bi' and re.match(r'^[a-zA-Z0-9_-]+$', p):
            return f'bi-{p}'
    if re.match(r'^[a-zA-Z0-9_-]+$', val):
        return f'bi-{val}'
    return val


class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = '__all__'
        widgets = {
            'platform': forms.Select(attrs={'class': 'form-select', 'id': 'id_platform'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'icon': forms.TextInput(attrs={'class': 'form-control icon-picker-input', 'id': 'id_icon', 'placeholder': 'e.g. bi-github, or paste <i class="bi bi-github"></i>'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_icon(self):
        icon = self.cleaned_data.get('icon', '')
        return clean_bootstrap_icon_class(icon)
