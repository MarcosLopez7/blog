from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignInForm(forms.Form):
    email = forms.CharField(
                max_length=200, 
                widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
                max_length=150, 
                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    first_name = forms.CharField(
                max_length=50, 
                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
                max_length=50, 
                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    email = forms.CharField(
                max_length=200, 
                widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password1 = forms.CharField(
                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']