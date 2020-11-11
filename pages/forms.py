from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Título'}),
            'content': forms.Textarea(attrs={}),
            'order': forms.NumberInput(attrs={}),
        }
        labels = {
            'title':'', 'content':'', 'order':''
        }