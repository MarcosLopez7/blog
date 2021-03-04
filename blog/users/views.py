from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

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
                login(request, user)

                return redirect("/")
        else:
            form = SignUpForm()

        context = {
            'form': form
        }

        return render(request, 'users/sign_up.html', context)
    else:
        return redirect('/')