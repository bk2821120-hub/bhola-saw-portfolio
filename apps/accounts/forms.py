from django import forms
from django.contrib.auth.forms import AuthenticationForm


class PortalLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Username',
            'autofocus': True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg pe-5',
            'placeholder': 'Password',
            'id': 'id_password',
        })
    )
