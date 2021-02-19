from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog

def index(request):
    return HttpResponse("Hola mundo! estàs entrando en los blogs")


def retrieve_blog(request, blog_id):
    blog = Blog.objects.filter(pk=blog_id)[0]
    print(str(blog.image))
    context = {
        "blog": blog,
        "image": str(blog.image)[7:]
    }
    return render(request, 'blogs/blog.html', context)