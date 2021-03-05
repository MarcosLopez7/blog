from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail

from .forms import SignUpForm


# Create your views here.
def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)

            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                send_mail(
                    'Gracias por registrate al blog', 
                    """
                    <h1>Gracias por registrarte</h1>
                    <p>Esperemos que los posts de este blog sean de tu agrado</p>
                    """,
                    settings.EMAIL_SENDER,
                    [user.email],
                    fail_silently=False
                    )

                login(request, user)

                return redirect(reverse('users:successful'))
        else:
            form = SignUpForm()

        context = {
            'form': form
        }

        return render(request, 'users/sign_up.html', context)
    else:
        return redirect('/')


def successful_registration(request):
    return render(request, 'users/successful_registration.html')