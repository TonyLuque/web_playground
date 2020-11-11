from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    # success_url = reverse_lazy('login') # No se puede concatenar, entoces se redefine el metodo get_success_url
    template_name = "registration/signup.html"

    def get_success_url(self):
        return reverse_lazy('login') + '?register'