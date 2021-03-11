from django.http import HttpResponse
from django.shortcuts import render

from posts.models import Post

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'index.html', context)

def unauthorized(request):
    return render(request, 'unauthorized.html')
