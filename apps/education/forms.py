from django import forms
from .models import Education

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        widgets = {
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
            'university_or_board': forms.TextInput(attrs={'class': 'form-control'}),
            'start_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'end_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'result': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'institution_logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_year = cleaned_data.get('start_year')
        end_year = cleaned_data.get('end_year')
        if start_year and end_year and start_year > end_year:
            self.add_error('end_year', 'End year cannot be earlier than start year.')
        return cleaned_data
