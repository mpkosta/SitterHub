from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView
from .forms import CustomLoginForm

urlpatterns = [
    path('registration/', RegisterView.as_view(), name='registration'),
    path('login/', LoginView.as_view(
        template_name='accounts/login.html',
        form_class=CustomLoginForm),
        name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]