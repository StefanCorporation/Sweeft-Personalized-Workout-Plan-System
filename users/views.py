from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView

from common.views import TitleMixin
from users.forms import UserLoginForm, UserRegistrationForm
from users.models import User


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Login'
   

class UserRegistrationView(TitleMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    title = 'Registration'



def profile(request):
    return render(request, 'users/profile.html')