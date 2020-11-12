from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    # success_url = reverse_lazy('login') # No se puede concatenar, entoces se redefine el metodo get_success_url
    template_name = "registration/signup.html"

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modificar en tiempo real para no dañar los que ya trae Django por defecto
        form.fields['username'].widget = forms.TextInput(attrs={'class':'name_class', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'name_class', 'placeholder':'email@dominio.com'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':'Repita la contraseña'})
        return  form

@method_decorator(login_required, name="dispatch")
class ProfileUpdate(UpdateView):
    # model = Profile # Se borra ya que viene dentro del formulario
    # fields = ['avatar', 'bio', 'link'] # Se quita ya que se llama en el ProfileForm del archivo forms.py
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # Recuperar el objeto que se va a editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

@method_decorator(login_required, name="dispatch")
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # Recuperar el objeto que se va a editar
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        form.fields['email'].widget = forms.EmailInput(attrs={'placeholder':'email'})
        return form