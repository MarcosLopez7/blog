from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .forms import SignUpForm, SignInForm
from .tokens import account_activation_token


def sign_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            form = SignInForm(request.POST)
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
        else:
            form = SignInForm()

        context = {
            'form': form
        }

        return render(request, 'users/sign_in.html', context)
    else:
        return redirect('/')

def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)

            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                url_site = get_current_site(request)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = account_activation_token.make_token(user),
                print(uid)
                print(token)
                message = render_to_string('users/email_validation.html', {
                            'user': user,
                            'domain': url_site,
                            'uid': uid,
                            'token': token[0],
                        })
                send_mail(
                    'Gracias por registrate al blog', 
                    message,
                    settings.EMAIL_SENDER,
                    [user.email],
                    fail_silently=False
                    )

                return redirect(reverse('users:successful'))
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
        return render(request, 'users/user_activated.html')
    else:
        return HttpResponse('¡Lo sentimos, el link es inválido!')


def successful_registration(request):
    return render(request, 'users/successful_registration.html')