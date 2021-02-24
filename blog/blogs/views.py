from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Blog
from .forms import BlogForm


def index(request):
    return HttpResponse("Hola mundo! estàs entrando en los blogs")


def create_blog(request):
    if request.user.is_authenticated:
        form = BlogForm()

        context = {
            'form': form
        }

        return render(request, 'blogs/blog_form.html', context)
    else:
        return redirect('/unauthorized')


def retrieve_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        "blog": blog
    }

    return render(request, 'blogs/blog.html', context)


def get_blogs(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(user=request.user)

        context = {
            'blogs': blogs 
        }

        return render(request, 'blogs/blog_list.html', context)
    else:
        return redirect('/unauthorized')