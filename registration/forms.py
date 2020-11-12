from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser valido")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya esta registrado.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar' : forms.ClearableFileInput(attrs={}),
            'bio' : forms.Textarea(attrs={'rows':3, 'placeholder':'Biografia'}),
            'link' : forms.URLInput(attrs={'placeholder':'http://link.com'})
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser valido")

    class Meta:
        model = User
        fields = ['email']

    # Si ponemos widgets como en la clase de arriba, se dañarian las validaciones que trae django en los campos
    # por defecto, por eso se hacen en el archivo views.py

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya esta registrado.")
        return email