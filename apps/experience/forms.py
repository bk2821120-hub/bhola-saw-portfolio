from django import forms
from .models import Experience

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'employment_type': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'currently_working': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'responsibilities': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'One responsibility per line'}),
            'skills_used': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Python, Django, MySQL'}),
            'company_logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        currently_working = cleaned_data.get('currently_working')
        if not currently_working and not end_date:
            self.add_error('end_date', 'Please provide an end date or select "Currently Working Here".')
        if start_date and end_date and start_date > end_date:
            self.add_error('end_date', 'End date cannot be earlier than start date.')
        return cleaned_data
