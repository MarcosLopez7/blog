from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Blog

def index(request):
    return HttpResponse("Hola mundo! estàs entrando en los blogs")


def retrieve_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        "blog": blog
    }
    
    return render(request, 'blogs/blog.html', context)
