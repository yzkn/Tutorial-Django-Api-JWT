from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
)
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'myaccapp/signup.html'


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('myaccapp:password_change_done')
    template_name = 'register/password_change_form.html'


class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'register/password_changed_done.html'
