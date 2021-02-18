from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog

def index(request):
    return HttpResponse("Hola mundo! estàs entrando en los blogs")


def retrieve_blog(request, blog_id):
    blog = Blog.objects.filter(id=blog_id)
    context = {
        "blog": blog
    }
    return render(request, 'polls/index.html', context)