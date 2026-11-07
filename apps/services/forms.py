from django import forms
from .models import Service
from apps.portfolio.forms import clean_bootstrap_icon_class


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['slug', 'created_at', 'updated_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Python Data Analysis'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brief 1-line overview of the service'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Detailed service explanation'}),
            'deliverables': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Deliverables (one per line, e.g.\nData cleaning and formatting\nPivot Tables and XLOOKUP)'}),
            'technologies': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Python, Pandas, NumPy, Matplotlib'}),
            'icon': forms.TextInput(attrs={'class': 'form-control icon-picker-input', 'id': 'id_icon', 'placeholder': 'e.g. bi-bar-chart-line'}),
            'starting_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Starting from $49 or Custom Quote'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_icon(self):
        icon = self.cleaned_data.get('icon', '')
        return clean_bootstrap_icon_class(icon)
