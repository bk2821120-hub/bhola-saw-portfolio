from django import forms
from .models import SkillCategory, Skill

class SkillCategoryForm(forms.ModelForm):
    class Meta:
        model = SkillCategory
        fields = ['name', 'display_order', 'active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

from apps.portfolio.forms import clean_bootstrap_icon_class

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'level': forms.Select(attrs={'class': 'form-select'}),
            'icon': forms.TextInput(attrs={'class': 'form-control icon-picker-input', 'id': 'id_icon', 'placeholder': 'e.g. bi-filetype-py, or paste <i class="bi bi-filetype-py"></i>'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_icon(self):
        icon = self.cleaned_data.get('icon', '')
        return clean_bootstrap_icon_class(icon)
