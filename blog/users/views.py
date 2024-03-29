import string
import random

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, logout

from .forms import SignUpForm, SignInForm, ResetPasswordForm, ChangePasswordForm
from .tokens import account_activation_token


def sign_in(request):
    if not request.user.is_authenticated:
        error_message = None

        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            form = SignInForm(request.POST)
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, 'Has iniciado sesión')
                return redirect("/")
            else:
                error_message = "Error al Iniciar Sesión: El email o la constraseña están incorrectas, por favor, verifica otra vez e intenta de nuevo"
        else:
            form = SignInForm()

        context = {
            'form': form,
            'error_message': error_message
        }

        return render(request, 'users/sign_in.html', context)
    else:
        return redirect('/')

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangePasswordForm(request.POST)

            if form.is_valid():
                old_password = form.cleaned_data['old_password']
                user = authenticate(request, username=request.user.email, password=old_password)

                if user is not None:
                    new_password = form.cleaned_data['new_password2']
                    user.set_password(new_password)
                    user.save()
                    login(request, user)
                    messages.info(request, 'La contraseña ha sido modificada exitosamente')
                    return redirect("/")
        else:
            form = ChangePasswordForm()

        context = {
            'form': form
        }

        return render(request, 'users/change_password.html', context)
    else:
        redirect('/unauthorized')

def reset_password(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = ResetPasswordForm(request.POST)

            if form.is_valid():
                email = form.cleaned_data['email']
                user = User.objects.get(email=email)
                """
                Gracias no1crate por tu aportaciòn a estas líneas de código
                """
                caracteres = string.ascii_letters + string.digits
                password = "".join(random.choices(caracteres, k=20))
                title = 'Cambio de contraseña'
                content = """
                    Dale click al siguiente link para que puedas cambiar tu contraseña
                """
                user.set_password(password)
                user.save()
                url_site = get_current_site(request)
                message = render_to_string('users/email_validation.html', {
                            'user': user,
                            'domain': url_site,
                            'uid': None,
                            'token': None,
                            'title': title,
                            'content': content,
                            'password': password
                        })
                send_mail(
                    'Cambio de contraseña', 
                    message,
                    settings.EMAIL_SENDER,
                    [email],
                    fail_silently=False
                    )

            return redirect(reverse('users:notification', args=['password-resetted']))
        else:
            form = ResetPasswordForm()

        context = {
            'form': form
        }

        return render(request, 'users/reset_password.html', context)

    else:
        return redirect('/')

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'Has cerrado sesión')
        return redirect('/')
    else:
        return redirect(reverse('user:sign-in'))

def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)

            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                title = 'Gracias por registrarte'
                content = """
                    Esperemos que los posts de este blog sean de tu agrado.\n\n
                    Por favor da click en el siguiente enlace para que podamos validar tu correo
                """
                url_site = get_current_site(request)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = account_activation_token.make_token(user),
                message = render_to_string('users/email_validation.html', {
                            'user': user,
                            'domain': url_site,
                            'uid': uid,
                            'token': token[0],
                            'title': title,
                            'content': content,
                            'password': None
                        })
                send_mail(
                    'Gracias por registrate al blog', 
                    message,
                    settings.EMAIL_SENDER,
                    [user.email],
                    fail_silently=False
                    )

                return redirect(reverse('users:notification', args=['registration']))
        else:
            form = SignUpForm()

        context = {
            'form': form
        }

        return render(request, 'users/sign_up.html', context)
    else:
        return redirect('/')

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect(reverse('users:notification', args=['activation']))
    else:
        return HttpResponse('¡Lo sentimos, el link es inválido!')

def notification_view(request, message):

    if message == 'registration':
        context = {
            'title': '¡Gracias por registrarte!',
            'content': """
                Te hemos enviado un correo electrónico para confirmar tu emial, 
                por favor, checa tu buzón de spam porque es probable que se encuentre ahí
            """,
            'footer': 'Muchas gracias',
            'message_type': 'success'
        }
    elif message == 'activation':
        context = {
            'title': '¡Correo Electrónico verificado!',
            'content': 'Has completado tu proceso de registro, puedes escribir y publicar en nuestros posts',
            'footer': 'Inicia Sesión para que uses la app',
            'message_type': 'success'
        }
    elif message == 'password-resetted':
        context = {
            'title': '¡Hemos cambiado tu contraseña!',
            'content': """
                Te hemos enviado un correo electrónico con la nueva contraseña que hemos generado por ti
            """,
            'footer': 'Por favor inicia sesión y cambia tu contraseña lo antes posible',
            'message_type': 'success'
        }
    else:
        context = {
            'title': '¡Uh Oh! Algo salió mal',
            'content': """
                No estamos seguros que pasó aquí
            """,
            'footer': 'Regresa al blog para no regresar aquí',
            'message_type': 'danger'
        }

    return render(request, 'users/user_message.html', context)