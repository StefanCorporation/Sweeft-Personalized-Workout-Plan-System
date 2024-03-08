from django.contrib.auth.forms import AuthenticationForm,  UserCreationForm
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True}))


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    username = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'required': True}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'required': True}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'required': True}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']