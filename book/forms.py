from .models import *
from django import forms



class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['user_name', 'slug', 'email',
                  'home_page','text', 'tags']

        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'home_page': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }