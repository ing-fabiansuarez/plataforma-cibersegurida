from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import StudentSignupForm

class StudentSignupView(CreateView):
    form_class = StudentSignupForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LogoutView):
    next_page = 'index'
