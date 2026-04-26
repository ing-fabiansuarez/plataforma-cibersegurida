from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import StudentSignupForm

from django.contrib.auth import login

class StudentSignupView(CreateView):
    form_class = StudentSignupForm
    success_url = reverse_lazy('index')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LogoutView):
    next_page = 'index'
