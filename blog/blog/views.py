from django.http import HttpResponse
from django.shortcuts import render

from posts.models import Post

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'index.html', context)

def terms_condition(request):
    return render(request, 'terms_condition.html')

def privacy(request):
    return render(request, 'privacy.html')

def unauthorized(request):
    return render(request, 'unauthorized.html')