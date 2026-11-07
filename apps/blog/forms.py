from django import forms
from .models import BlogPost, BlogTag

class BlogTagForm(forms.ModelForm):
    class Meta:
        model = BlogTag
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ['slug', 'created_at', 'updated_at', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 15}),
            'tags': forms.CheckboxSelectMultiple(),
            'published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'published_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
