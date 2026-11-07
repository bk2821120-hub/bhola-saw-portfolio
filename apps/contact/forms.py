from django import forms
from .models import ContactMessage

BUDGET_CHOICES = [
    ('', 'Select Project Budget (Optional)'),
    ('< $100', '< $100 (Small Task / Fix)'),
    ('$100 - $300', '$100 - $300 (Standard Project)'),
    ('$300 - $500', '$300 - $500 (Comprehensive Project)'),
    ('$500+', '$500+ (Full-Scale Application / Pipeline)'),
    ('Negotiable', 'Negotiable / To Be Discussed'),
]

TIMELINE_CHOICES = [
    ('', 'Expected Timeline (Optional)'),
    ('Urgent (1-3 days)', 'Urgent (1 - 3 days)'),
    ('Within 1 week', 'Within 1 week'),
    ('1 - 2 weeks', '1 - 2 weeks'),
    ('1 month+', '1 month+'),
    ('Flexible', 'Flexible timeline'),
]


class ContactForm(forms.ModelForm):
    service = forms.CharField(
        required=False,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_service'})
    )
    budget = forms.ChoiceField(
        choices=BUDGET_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_budget'})
    )
    timeline = forms.ChoiceField(
        choices=TIMELINE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_timeline'})
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'service', 'budget', 'timeline', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@email.com'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject (e.g. Project Inquiry)'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe your project requirements, goals, or questions in detail...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            from apps.services.models import Service
            active_services = list(Service.objects.filter(is_active=True).values_list('title', flat=True))
        except Exception:
            active_services = []

        choices = [('', 'Select a Service (Optional)')]
        for s in active_services:
            choices.append((s, s))
        choices.append(('Custom Project / Consultation', 'Custom Project / Consultation'))

        val = None
        if self.is_bound:
            val = self.data.get('service')
        elif self.initial:
            val = self.initial.get('service')
        if val and val not in [c[0] for c in choices]:
            choices.insert(1, (val, val))

        self.fields['service'].widget.choices = choices

    def clean(self):
        cleaned_data = super().clean()
        subject = cleaned_data.get('subject')
        service = cleaned_data.get('service')
        if not subject:
            cleaned_data['subject'] = f"Project Inquiry: {service}" if service else "General Project Inquiry"
        return cleaned_data
