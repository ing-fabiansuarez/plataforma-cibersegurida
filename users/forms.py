from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.utils.translation import gettext_lazy as _

class StudentSignupForm(UserCreationForm):
    first_name = forms.CharField(label=_("Nombre"), max_length=30, required=True)
    last_name = forms.CharField(label=_("Apellido"), max_length=30, required=True)
    email = forms.EmailField(label=_("Correo electrónico"), required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.Role.STUDENT
        if commit:
            user.save()
        return user
