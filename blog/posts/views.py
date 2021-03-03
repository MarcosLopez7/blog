from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse

from .models import Post
from .forms import PostForm

def index(request):
    return HttpResponse("Hola mundo! estàs entrando en los blogs")


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)

            if form.is_valid():
                post_instance = form.save(commit=False)
                post_instance.user = request.user
                post_instance.save()

                return redirect(reverse('posts:get', args=[post_instance.pk]))
        else:
            form = PostForm()

        context = {
            'form': form 
        }

        return render(request, 'posts/post_form.html', context)
    else:
        return redirect('/unauthorized')


def get_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        "post": post
    }

    return render(request, 'posts/post.html', context)


def get_posts(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(user=request.user)

        context = {
            'list_title': 'My post list',
            'posts': posts 
        }

        return render(request, 'posts/post_list.html', context)
    else:
        return redirect('/unauthorized')