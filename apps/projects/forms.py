from django import forms
from .models import Project, ProjectTechnology

class ProjectForm(forms.ModelForm):
    technologies = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Python, Django, MySQL (comma separated)'}),
        help_text='Enter technologies separated by commas'
    )
    class Meta:
        model = Project
        exclude = ['slug', 'created_at', 'updated_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'problem_statement': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'solution': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control'}),
            'live_demo_url': forms.URLInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            existing = ', '.join(self.instance.technologies.values_list('name', flat=True))
            self.fields['technologies'].initial = existing

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date and end_date and start_date > end_date:
            self.add_error('end_date', 'End date cannot be earlier than start date.')
        return cleaned_data
