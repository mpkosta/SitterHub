from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    template_name = 'accounts/registration.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')