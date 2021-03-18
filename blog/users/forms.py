from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User


class ResetPasswordForm(forms.Form):
    email = forms.CharField(
                max_length=200, 
                widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )

    def clean_email(self):
        """
        Validar que el email enviado esté registrado
        """
        data = self.cleaned_data['email']
        try:
            User.objects.get(email=data)
        except:
            raise ValidationError("Lo sentimos, el email no está registrado")

        return data


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña actual'})
    )
    new_password1 = forms.CharField(
                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nueva contraseña'})
    )
    new_password2 = forms.CharField(
                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar nueva contraseña'})
    )

    def clean_new_password1(self):
        """
        Validar que la contraseña coincida con el primer password
        """
        password_1 = self.cleaned_data['new_password1']

        validate_password(password_1)

        return password_1

    def clean_new_password2(self):
        """
        Validar que la contraseña coincida con el primer password
        """
        password_1 = self.data['new_password1']
        password_2 = self.cleaned_data['new_password2']

        if password_2 != password_1:
            raise ValidationError("Lo sentimos, las contraseñas no coinciden")

        return password_2


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

    def clean_email(self):
        email = self.cleaned_data['email']

        users = User.objects.filter(email=email)

        if len(users) > 0:
            raise ValidationError("El correo electrónico proporcionado ya ha sido reegistrado, por favor ingresa otro")

        return email

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']